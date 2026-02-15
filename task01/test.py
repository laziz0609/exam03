from datetime import datetime
from book import Book

# Kitob yaratish
book = Book(1, "Clean Code", "Robert Martin", 464)

# Kitobni berish
book.borrow("Ali")
print(book.borrower)  # "Ali"
print(book.is_borrowed)  # True

# Kitobni qaytarish
book.return_book()
print(book.borrower)  # None

# Nomini o'zgartirish
book.change_title("Clean Code 2nd Edition")

# Info olish
info = book.info()
print(info["status"])  # "available"
print(info["times_borrowed"])  # 1

# Dunder metodlar
print(book)  # <Book Clean Code 2nd Edition>
print(len(book))  # 464
print(bool(book))  # True

# Arxivlash
book.archive()
print(bool(book))  # False