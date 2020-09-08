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
    ThumbnailCard,
    CardImage
    
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
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=33.8971058%2C35.4833635&radius=1000&type=hospital&fields=name%2Cformatted_address%2Cformatted_phone_number&key={}".format(DefaultConfig.API_KEY)
        response = requests.get(url)
        if response.status_code == 200:
            hospitalsList = []
            for i in range(4):
                hospital = []
                result = response.json()['results'][i]
                name = result['name']
                vicinity = result['vicinity']
                place_id = result['place_id']
                openNow = result.get('opening_hours')
                link = "https://www.google.com/maps/place/?q=place_id:{}".format(place_id)
                photoreference = result.get("photos")
                if(photoreference):
                    photoreference = photoreference[0].get('photo_reference')
                if openNow:
                    openNow = openNow.get('open_now')
                    if openNow == True:
                        openNow = "Open"
                    else:
                        openNow = "Closed"
                else:
                    openNow = "opening hours not registered"
                rating = result.get('rating')
                if rating:
                    pass
                else:
                    rating = "No ratings available"
                user_ratings_total = result.get('user_ratings_total')
                if user_ratings_total:
                    pass
                else:
                    user_ratings_total = "N/A"
                Imageurl = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(photoreference,DefaultConfig.API_KEY,)
                hospital.append(name)
                hospital.append(vicinity)
                hospital.append(openNow)
                hospital.append(rating)
                hospital.append(user_ratings_total)
                hospital.append(link)
                hospital.append(Imageurl)
                hospitalsList.append(hospital)
            for hospital in hospitalsList:
                reply = MessageFactory.list([])
                reply.attachments.append(create_thumbnail_card(hospital))
                await turn_context.send_activity(reply)
        elif response.status_code == 404:
            print('Not Found.')

    else:
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=33.8971058,35.4833635&radius=1000&type=pharmacy&fields=name,formatted_address,photo,vicinity&key={}".format(DefaultConfig.API_KEY)
        response = requests.get(url)
        if response.status_code == 200:
            pharmacysList = []
            for i in range(4):
                pharmacy = []
                result = response.json()['results'][i]
                name = result['name']
                vicinity = result['vicinity']
                place_id = result['place_id']
                openNow = result.get('opening_hours')
                link = "https://www.google.com/maps/place/?q=place_id:{}".format(place_id)
                photoreference = result.get("photos")
                if(photoreference):
                    photoreference = photoreference[0].get('photo_reference')
                if openNow:
                    openNow = openNow.get('open_now')
                    if openNow == True:
                        openNow = "Open"
                    else:
                        openNow = "Closed"
                else:
                    openNow = "<not registered>"
                rating = result.get('rating')
                if rating:
                    pass
                else:
                    rating = "No ratings available"
                user_ratings_total = result.get('user_ratings_total')
                if user_ratings_total:
                    pass
                else:
                    user_ratings_total = "N/A"
                Imageurl = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(photoreference,DefaultConfig.API_KEY,)
                pharmacy.append(name)
                pharmacy.append(vicinity)
                pharmacy.append(openNow)
                pharmacy.append(rating)
                pharmacy.append(user_ratings_total)
                pharmacy.append(link)
                pharmacy.append(Imageurl)
                pharmacysList.append(pharmacy)
            for pharmacy in pharmacysList:
                reply = MessageFactory.list([])
                reply.attachments.append(create_thumbnail_card(pharmacy))
                await turn_context.send_activity(reply)
        elif response.status_code == 404:
            print('Not Found.')


def create_thumbnail_card(mylist) -> Attachment:
        card = ThumbnailCard(
            title=mylist[0],
            subtitle=mylist[1],
            text = "Ratings: {} ({} ratings) \n\n opening hours: {}".format(mylist[3],mylist[4],mylist[2]),
            images=[
                CardImage(
                    url=mylist[6]
                )
            ],
            buttons=[
                CardAction(
                    type=ActionTypes.open_url,
                    title="Get directions",
                    value=mylist[5],
                )
            ],
        )
        return CardFactory.thumbnail_card(card)