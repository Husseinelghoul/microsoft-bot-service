from botbuilder.core import ActivityHandler, MessageFactory, TurnContext, CardFactory
from botbuilder.schema import (
    ChannelAccount,
    HeroCard,
    CardAction,
    ActivityTypes,
    Attachment,
    AttachmentData,
    Activity,
    ActionTypes,
)
HPlist = ["[HP]","[HOSP]","[PHA]"]
async def HP_display_options(turn_context: TurnContext,option):
    """
    Create a HeroCard with options for the user to interact with the bot.
    :param turn_context:
    :return:
    """
    if option=="[HP]":
        card = HeroCard(
            text="Please choose one of the following options",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. Hospitals", value="[HOSP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. Pharmacies", value="[PHA]"
                )
            ],
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))    
    else:
        reply = "<Under construction>"

    await turn_context.send_activity(reply)