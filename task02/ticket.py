from seat import Seat

class Ticket:
    def __init__(self, seat: Seat, owner: str):
        self.seat = seat
        self.owner = owner


    @staticmethod
    def is_correct(seat: any, owner: any) -> str:
        if type(seat) != Seat:
            raise Exception("seat Seat classidan yaratilishi kerak")
        
        if type(owner) != str:
            raise Exception("owner str bo'lishi kerak")

        if not owner:
            raise Exception("owner bo'sh str bo'lmasligi kerak")