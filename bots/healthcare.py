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
import requests
import json
from config import DefaultConfig
HPlist = ["[HOSP]","[PHA]"]
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


async def getProvider(turn_context: TurnContext,type):
    if type == "[HOSP]":
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=33.8971058,35.4833635&radius=1000&type=hospital&fields=name,formatted_address,photo,vicinity&key={}".format(DefaultConfig.API_KEY)
    else:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=33.8971058,35.4833635&radius=1000&type=pharmacy&fields=name,formatted_address,photo,vicinity&key={}".format(DefaultConfig.API_KEY)
    response = requests.get(url)
    mylist = []
    if response.status_code == 200:
        for result in response.json()['results']:
            mylist.append(result['name'])
    elif response.status_code == 404:
        print('Not Found.')
    reply = ""
    for i in range(int(len(mylist)/2)):
        reply =    reply + str(mylist[i]) + '\n\n'
    await turn_context.send_activity(reply) 
#test