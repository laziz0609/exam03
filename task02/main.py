
from cinemasession import CinemaSession
from seat import Seat

# 2. Seans yaratish
session = CinemaSession("Avatar 2", 5)

# 3. Bo'sh joylarni ko'rish
print(session.available_seats())  # [1, 2, 3, 4, 5]

# 4. Bron qilish
ticket1 = session.book_seat(3, "Ali")
print(ticket1.owner)              # "Ali"
print(ticket1.seat.number)        # 3
print(ticket1.seat.is_taken)      # True

# 5. Bo'sh joylar
print(session.available_seats())  # [1, 2, 4, 5]

# 6. Yana bron
ticket2 = session.book_seat(1, "Vali")
print(session.available_seats())  # [2, 4, 5]

# 7. Olingan joyga yana bron (xato)
try:
    session.book_seat(3, "Sardor")
except Exception as e:
    print("Xato: O'rin allaqachon olingan!")

# 8. String representation
print(session)  # CinemaSession: Avatar 2 (5 seats)

# 9. Bookings ro'yxatini ko'rish
print(f"Jami bron: {len(session.bookings)}")  # 2
for ticket in session.bookings:
    print(f"O'rin {ticket.seat.number}: {ticket.owner}")