#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "0bc99f6b-7b4c-4e06-b0f7-1478dc20b3e7")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "wzuXy7W4di8IW4.NC2Zb3_x~R_N3t7J4Ft")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "24bed8e8-7bd7-47e1-9461-b80cc5011a51")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "e074dd5e-82a1-4065-9724-21f9b0cb758c")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://globemedbot-poc.azurewebsites.net/qnamaker")
    DB_ENDPOINT_HOST = "eu-cdbr-west-03.cleardb.net"
    DB_ENDPOINT_USER = "b37418f3155fc2"
    DB_ENDPOINT_PSSWD = "2cbca5e6"
    DB_NAME = "heroku_440429e2a845dd0"
    API_KEY = "AIzaSyDFKz8Ao3_1ukJj-ZvZMuRck_OaTRg7dq8"