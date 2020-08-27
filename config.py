#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    QNA_KNOWLEDGEBASE_ID = os.environ.get("QnAKnowledgebaseId", "24bed8e8-7bd7-47e1-9461-b80cc5011a51")
    QNA_ENDPOINT_KEY = os.environ.get("QnAEndpointKey", "e074dd5e-82a1-4065-9724-21f9b0cb758c")
    QNA_ENDPOINT_HOST = os.environ.get("QnAEndpointHostName", "https://globemedbot-poc.azurewebsites.net/qnamaker")
