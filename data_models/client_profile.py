class ClientProfile:
    def __init__(self, name: str = None, cardno: int = 0,
                claimno: int = 0, ETA : int = 0, status: str = None, description: str = None):
        self.name = name
        self.cardno = cardno
        self.claimno = claimno
        self.status = status
        self.ETA = ETA
        self.description = description
