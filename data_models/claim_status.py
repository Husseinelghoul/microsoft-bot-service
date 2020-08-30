from enum import Enum


class ClaimQuestion(Enum):
    CLAIMNO = 1
    CARDNO = 2
    NONE = 5

class ClaimConversationFlow:
    def __init__(
        self, last_question_asked: ClaimQuestion = ClaimQuestion.NONE,
    ):
        self.last_question_asked = last_question_asked
