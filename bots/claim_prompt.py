# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from datetime import datetime
from recognizers_number import recognize_number, Culture
from recognizers_date_time import recognize_datetime

from botbuilder.core import (
    ActivityHandler,
    ConversationState,
    TurnContext,
    UserState,
    MessageFactory,
)
from config import DefaultConfig
import mysql.connector
def createSQL():
    mydb = mysql.connector.connect(
  host= DefaultConfig.DB_ENDPOINT_HOST,
  user =DefaultConfig.DB_ENDPOINT_USER,
  password= DefaultConfig.DB_ENDPOINT_PSSWD,
  database= DefaultConfig.DB_NAME)
    return mydb

from data_models import ClaimConversationFlow, ClaimQuestion, ClientProfile
class ValidationResult:
    def __init__(
        self, is_valid: bool = False, value: object = None, message: str = None
    ):
        self.is_valid = is_valid
        self.value = value
        self.message = message
def validate_claimno(user_input: str) -> ValidationResult:
    mydb = createSQL();
    mycursor = mydb.cursor()
    sql = "SELECT claimno FROM claims WHERE claimno = {}".format(int(user_input))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult)==0:
        return ValidationResult(
            is_valid=False,
            message="This claim number is not recognized, please try again",
        )
    mydb.close()
    return ValidationResult(is_valid=True, value=int(user_input))

def validate_cardno(user_input: str,_claimno) -> ValidationResult:
    mydb = createSQL();
    results = recognize_number(user_input, Culture.English)
    for result in results:
        if "value" in result.resolution:
            cardno = int(result.resolution["value"])
            mycursor = mydb.cursor()
            sql = "SELECT * FROM claims WHERE cardno = {} AND claimno = {}".format(int(user_input),_claimno)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if len(myresult)>0:
                mydb.close()
                return ValidationResult(is_valid=True, value=cardno)
    return ValidationResult(
        is_valid=False, message="It appears that there is no claim number associated with this card number . Please try a different card number"
    )
def getName(cardno):
    mydb = createSQL()
    mycursor = mydb.cursor()
    sql = "SELECT name FROM clients WHERE cardno = {}".format(cardno)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult[0][0]
def getStatus(claimno):
    mydb = createSQL()
    mycursor = mydb.cursor()
    sql = "SELECT status FROM claims WHERE claimno = {}".format(claimno)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult[0][0]
def getETA(claimno):
    mydb = createSQL()
    mycursor = mydb.cursor()
    sql = "SELECT ETA FROM claims WHERE claimno = {}".format(claimno)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult[0][0]
def getDescription(claimno):
    mydb = createSQL()
    mycursor = mydb.cursor()
    sql = "SELECT description FROM claims WHERE claimno = {}".format(claimno)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult[0][0]