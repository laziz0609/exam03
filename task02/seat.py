class Seat:
    def __init__(self, number: int) -> None:
        self.is_correct(number)

        self.number = number
        self.is_taken = False


    @staticmethod
    def is_correct(num: any) -> None:
        if type(num) != int:
            raise Exception("o'rin raqami butun son bo'lishi kerak")
        
        if num < 1:
            raise Exception("o'rin raqami musbat bo'lishligi kerak (nolga ham teng bo'lmasligi kerak)")