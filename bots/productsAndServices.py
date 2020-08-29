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
import mysql.connector
from config import DefaultConfig
mydb = mysql.connector.connect(
  host= DefaultConfig.DB_ENDPOINT_HOST,
  user =DefaultConfig.DB_ENDPOINT_USER,
  password= DefaultConfig.DB_ENDPOINT_PSSWD,
  database= DefaultConfig.DB_NAME
)
productsList = ["[PS]","[PRODUCTS]","[IAF]","[IP]","[GROUPS]","[SP]","[TP]","[MUP]","[TPP]","[DNP]","[TMP]","[NSOP]","[TPCP]","[TEP]"]
servicesList = ["[SERVICES]","[IHS]","[HBM]","[PBM]","[ACTUARIAL]","[PUMA]","[AAA]","[ESMP]","[TIP]","[IPMI]","[PM]","[MSM]","[DDM]","[SM]","[ASM]"]
async def PS_display_options(turn_context: TurnContext,option):
    """
    Create a HeroCard with options for the user to interact with the bot.
    :param turn_context:
    :return:
    """
    if option=="[PS]":
        card = HeroCard(
            text="Please choose one of the following options",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. Products", value="[PRODUCTS]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. Services", value="[SERVICES]"
                )
            ],
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option=="[PRODUCTS]":
        card = HeroCard(
            text="Please choose one of the following options",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. INDIVIDUALS AND FAMILIES PRODUCTS", value="[IAF]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. INTERNATIONAL PRODUCTS", value="[IP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="3. GROUPS PRODUCTS", value="[GROUPS]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="4. SPECIALIZED PRODUCTS", value="[SP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="5. TRAVEL PRODUCTS", value="[TP]"
                )  
            ],
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option=="[IAF]":
        card = HeroCard(
            text="Please choose one of the following options",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. THE PERPETUAL PLAN  ", value="[TPP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. THE MUTUAL UPGRADED PLAN", value="[MUP]"
                )  
            ],
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option=="[GROUPS]":
        card = HeroCard(
            text="Please choose one of the following options",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. THE DELTA NSSF PLAN", value="[DNP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. THE THE MEDCARE PLAN", value="[TMP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="3. THE NSSF OPT OUT PLAN", value="[NSOP]"
                ) 
            ], 
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option=="[SP]":
        card = HeroCard(
            text="Please choose one of the following options",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. THE PERPETUAL CONVERSION PLAN", value="[TPCP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. THE EXPATCARE PLAN", value="[TEP]"
                )
            ], 
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option == "[TPP]":
        reply = querry(11)
    elif option == "[MUP]":
        reply = querry(21)
    elif option == "[IP]":
        reply = querry(31)
    elif option == "[TP]":
        reply = querry(41)
    elif option == "[DNP]":
        reply = querry(51)
    elif option == "[TMP]":
        reply = querry(61)
    elif option == "[NSOP]":
        reply = querry(71)
    elif option == "[TPCP]":
        reply = querry(81)
    elif option == "[TEP]":
        reply = querry(91)
    elif option == "[SERVICES]":
        card = HeroCard(
            text="Please choose one of the following options",
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. INTERNATIONAL HEALTH SERVICES", value="[IHS]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. HEALTHCARE BENEFITS MANAGEMENT", value="[HBM]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="3. PHARMACY BENEFITS MANAGEMENT", value="[PBM]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="4. ACTUARIAL", value="[ACTUARIAL]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="5. PUMA", value="[PUMA]"
                )  
            ],
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option == "[PUMA]":
        card = HeroCard(
            text='''We value every applicant and we have established a solid strategy where even the
            applicants with unfavorable health conditions can receive coverage under specific terms.
            Our models can be used to price substandard risks and our systems can serve to apply coverage
            conditions at the most detailed level. Together they provide our clients with the capability tO
            reach all market segments while maintaining profitability.''',
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. Production Module", value="[PM]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. Medical Scoring Module", value="[MSM]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="3. Deep Dive Module", value="[DDM]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="4. Simulator Module", value="[SM]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="5. Actuarial Service Module", value="[ASM]"
                )  
            ],
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option == "[IHS]":
        card = HeroCard(
            text='''GlobeMed offers a wide range of services to provide your members access to healthcare around the world.
            Through GlobeMed Assist, our 24/7 call center, we can ensure that your members get the medical and assistance services needed anytime anywhere.''',
            buttons=[
                CardAction(
                    type=ActionTypes.im_back, title="1. Access and Assistance", value="[AAA]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="2. Expert Second Medical Opinion", value="[ESMP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="3. Travel Insurance Programs", value="[TIP]"
                ),
                CardAction(
                    type=ActionTypes.im_back, title="4. International Private Medical Insurance Programs (IPMI)", value="[IPMI]"
                ) 
            ],
        )
        reply = MessageFactory.attachment(CardFactory.hero_card(card))
    elif option == "[AAA]":
        reply =  querry(101)
    elif option == "[ESMP]":
        reply = querry(111)
    elif option == "[TIP]":
        reply = querry(111)
    elif option == "[IPMI]":
        reply = querry(121)
    elif option == "[IPMI]":
        reply = querry(131)
    elif option == "[HBM]":
        reply = querry(141)
    elif option == "[PBM]":
        reply = querry(151)
    elif option == "[ACTUARIAL]":
        reply = querry(161)
    elif option == "[PM]":
        reply = querry(171)
    elif option == "[MSM]":
        reply = querry(181)
    elif option == "[SM]":
        reply = querry(191)
    elif option == "[ASM]":
        reply = querry(201)
    elif option == "[DDM]":
        reply = querry(211)
    else:
        reply = "<Under construction>"
    await turn_context.send_activity(reply)

def querry(x):
    mycursor = mydb.cursor()
    sql = "SELECT description FROM products_services WHERE id = {}".format(x)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult[0][0]
