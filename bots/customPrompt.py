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

from data_models import ConversationFlow, Question, UserProfile

class ValidationResult:
    def __init__(
        self, is_valid: bool = False, value: object = None, message: str = None
    ):
        self.is_valid = is_valid
        self.value = value
        self.message = message
def validate_name(user_input: str) -> ValidationResult:
    if not user_input:
        return ValidationResult(
            is_valid=False,
            message="Please enter a name that contains at least one character.",
        )

    return ValidationResult(is_valid=True, value=user_input)

def validate_age(user_input: str) -> ValidationResult:
    # Attempt to convert the Recognizer result to an integer. This works for "a dozen", "twelve", "12", and so on.
    # The recognizer returns a list of potential recognition results, if any.
    results = recognize_number(user_input, Culture.English)
    for result in results:
        if "value" in result.resolution:
            age = int(result.resolution["value"])
            if 18 <= age <= 120:
                return ValidationResult(is_valid=True, value=age)

    return ValidationResult(
        is_valid=False, message="Please enter an age between 18 and 120."
    )

def validate_date(user_input: str) -> ValidationResult:
    try:
        # Try to recognize the input as a date-time. This works for responses such as "11/14/2018", "9pm",
        # "tomorrow", "Sunday at 5pm", and so on. The recognizer returns a list of potential recognition results,
        # if any.
        results = recognize_datetime(user_input, Culture.English)
        for result in results:
            for resolution in result.resolution["values"]:
                if "value" in resolution:
                    now = datetime.now()

                    value = resolution["value"]
                    if resolution["type"] == "date":
                        candidate = datetime.strptime(value, "%Y-%m-%d")
                    elif resolution["type"] == "time":
                        candidate = datetime.strptime(value, "%H:%M:%S")
                        candidate = candidate.replace(
                            year=now.year, month=now.month, day=now.day
                        )
                    else:
                        candidate = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

                    # user response must be more than an hour out
                    diff = candidate - now
                    if diff.total_seconds() >= 3600:
                        return ValidationResult(
                            is_valid=True,
                            value=candidate.strftime("%y-%m-%d"),
                        )

        return ValidationResult(
            is_valid=False,
            message="I'm sorry, please enter a date at least an hour out.",
        )
    except ValueError:
        return ValidationResult(
            is_valid=False,
            message="I'm sorry, I could not interpret that as an appropriate "
            "date. Please enter a date at least an hour out.",
        )
def validate_phoneNum(user_input: str) -> ValidationResult:
    phoneNum = user_input
    if (phoneNum[:2] in ["03","76","81","71","70","78"]) and (len(phoneNum) == 8):
        return ValidationResult(is_valid=True, value=phoneNum)
    return ValidationResult(
        is_valid=False, message="Your phone number should contain 8 numbers and start with 03, 70, 71, 76, 78 or 81"
    )
