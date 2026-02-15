from seat import Seat
from ticket import Ticket

class CinemaSession:
    
    def __init__(self, movie_title: str, total_seats: int) -> None:
        self.is_correct_constructor(movie_title, total_seats)

        self.movie_title = movie_title
        self.total_seats = total_seats
        self.seats: list[Seat] = []
        self.bookings: list[Ticket] =[]

        self.seats = []
        for i in range(1, total_seats + 1):
            self.seats.append(Seat(i))

    
    def available_seats(self) -> list[int]:
        result = []
        for seat in self.seats:
            if not seat.is_taken:
                result.append(seat.number)
        return result
    

    def book_seat(self, seat_number: int, user: str) -> Ticket:
        if seat_number < 1 or seat_number > self.total_seats:
            raise Exception(f"bunday raqamdagi seat mavjud emas (1 ≤ seat ≤ {self.total_seats})")
        
        for seat in self.seats:
            if seat.number == seat_number:
                if seat.is_taken:
                    raise Exception(f"{seat_number} joyi band qilingan")
                
                else:
                    seat.is_taken = True
                    ticket = Ticket(seat, user)
                    self.bookings.append(ticket)

                    return ticket


    def __str__(self):
        return f"CinemaSession: {self.movie_title} ({self.total_seats} seats)"



    @staticmethod
    def is_correct_constructor(movie_title: any, total_seats: any) -> None:
        if type(movie_title) != str:
            raise Exception("movia title str bo'lishi kerak")
        
        if not movie_title:
            raise Exception("movia title bo'sh bo'lamsligi kerak")
        
        if type(total_seats) != int:
            raise Exception("total seats int bo'lishi kerak")
        
        if total_seats < 1:
            raise Exception("totao seats 0 dan katta bo'lishligi kerak")


