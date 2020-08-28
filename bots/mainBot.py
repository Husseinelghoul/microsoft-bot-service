# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions
from .customPrompt import *
from config import DefaultConfig
from botbuilder.core import (
    ActivityHandler,
    ConversationState,
    TurnContext,
    UserState,
    MessageFactory,
)


class mainBot(ActivityHandler):
    def __init__(self, config: DefaultConfig, conversation_state: ConversationState, user_state: UserState,promptInput = False):
        self.qna_maker = QnAMaker(
            QnAMakerEndpoint(
                knowledge_base_id=config.QNA_KNOWLEDGEBASE_ID,
                endpoint_key=config.QNA_ENDPOINT_KEY,
                host=config.QNA_ENDPOINT_HOST,
            )
        )
        self.promptInput = promptInput
        if conversation_state is None:
            raise TypeError(
                "[CustomPromptBot]: Missing parameter. conversation_state is required but None was given"
            )
        if user_state is None:
            raise TypeError(
                "[CustomPromptBot]: Missing parameter. user_state is required but None was given"
            )

        self.conversation_state = conversation_state
        self.user_state = user_state

        self.flow_accessor = self.conversation_state.create_property("ConversationFlow")
        self.profile_accessor = self.user_state.create_property("UserProfile")      
    async def on_members_added_activity(self, members_added: [ChannelAccount], turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                #Welcome message
                await turn_context.send_activity(
                    "Welcome to  GlobeMed Bot, Ask me a question and I will try "
                    "to answer it."
                )
                """
                Create and sends an activity with suggested actions to the user. When the user
                clicks one of the buttons the text value from the "CardAction" will be displayed
                in the channel just as if the user entered the text. There are multiple
                "ActionTypes" that may be used for different situations.
                """
                reply = MessageFactory.text('''Alternatively I can help you finding a healthcare provider,
                                            booking an appointment, checking your claim status and I could show you our products and services.''')
                reply.suggested_actions = SuggestedActions(
                    actions=[
                        CardAction(title="Healthcare Provider", type=ActionTypes.im_back, value="[HP]"),
                        CardAction(title="Products and Services", type=ActionTypes.im_back, value="[PS]"),
                        CardAction(title="Book an Appoitment", type=ActionTypes.im_back, value="[BA]"),
                        CardAction(title="Claim Status",type=ActionTypes.im_back, value="[CS]")
                    ]
                )
                await turn_context.send_activity(reply)
                
                
    async def on_message_activity(self, turn_context: TurnContext):
        if (
            turn_context.activity.attachments
            and len(turn_context.activity.attachments) > 0
        ):
            await self._handle_incoming_attachment(turn_context)
        else:
            await self.handle_user_msg(turn_context)           
    async def handle_user_msg(self, turn_context: TurnContext):
        msg = turn_context.activity.text
        if msg == "[BA]" or self.promptInput:
            self.promptInput = True
                # Get the state properties from the turn context.
            profile = await self.profile_accessor.get(turn_context, UserProfile)
            flow = await self.flow_accessor.get(turn_context, ConversationFlow)

            await self._fill_out_user_profile(flow, profile, turn_context)

            # Save changes to UserState and ConversationState
            await self.conversation_state.save_changes(turn_context)
            await self.user_state.save_changes(turn_context)
        else:
            # The QnA Maker service.
            response = await self.qna_maker.get_answers(turn_context)
            if response and len(response) > 0:
                await turn_context.send_activity(MessageFactory.text(response[0].answer))
            else:
                await turn_context.send_activity("No QnA Maker answers were found.")
    async def _fill_out_user_profile(self, flow: ConversationFlow, profile: UserProfile, turn_context: TurnContext):
        user_input = turn_context.activity.text.strip()

        # ask for name
        if flow.last_question_asked == Question.NONE:
            await turn_context.send_activity(
                MessageFactory.text("Let's get started. What is your name?")
            )
            flow.last_question_asked = Question.NAME

        # validate name then ask for age
        elif flow.last_question_asked == Question.NAME:
            validate_result = validate_name(user_input)
            if not validate_result.is_valid:
                await turn_context.send_activity(
                    MessageFactory.text(validate_result.message)
                )
            else:
                profile.name = validate_result.value
                await turn_context.send_activity(
                    MessageFactory.text(f"Hi {profile.name}")
                )
                await turn_context.send_activity(
                    MessageFactory.text("How old are you?")
                )
                flow.last_question_asked = Question.AGE
        # validate age then ask for phone number
        elif flow.last_question_asked == Question.AGE:
            validate_result = validate_age(user_input)
            if not validate_result.is_valid:
                await turn_context.send_activity(
                    MessageFactory.text(validate_result.message)
                )
            else:
                profile.age = validate_result.value
                await turn_context.send_activity(
                    MessageFactory.text(f"I have your age as {profile.age}.")
                )
                await turn_context.send_activity(
                    MessageFactory.text("What's your phone number?")
                )
                flow.last_question_asked = Question.PHONENUM
        # validate phone number then ask for date
        elif flow.last_question_asked == Question.PHONENUM:
            validate_result = validate_phoneNum(user_input)
            if not validate_result.is_valid:
                await turn_context.send_activity(
                    MessageFactory.text(validate_result.message)
                )
            else:
                profile.phoneNum = validate_result.value
                await turn_context.send_activity(
                    MessageFactory.text(f"I have your phone number as {profile.phoneNum}")
                )
                await turn_context.send_activity(
                    MessageFactory.text("When would you like to have your meeting?")
                )
                flow.last_question_asked = Question.DATE

        # validate date and wrap it up
        elif flow.last_question_asked == Question.DATE:
            validate_result = validate_date(user_input)
            if not validate_result.is_valid:
                await turn_context.send_activity(
                    MessageFactory.text(validate_result.message)
                )
            else:
                profile.date = validate_result.value
                await turn_context.send_activity(
                    MessageFactory.text(
                        f"Your meeting is scheduled for {profile.date}."
                    )
                )
                await turn_context.send_activity(
                    MessageFactory.text(
                        f"Thanks for completing your reservation {profile.name}."
                    )
                )
                #TODO: Implement SQL Logic
                print(profile.name,profile.date,profile.age,profile.phoneNum)
                flow.last_question_asked = Question.NONE
                self.promptInput = False