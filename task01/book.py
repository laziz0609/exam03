from datetime import datetime


class Book:
    def __init__(self, id: int, title: str, author: str, pages: int) -> None:
        self.is_correct_item(id, title, author, pages)
        
        self.id: int = id
        self.title: str = title.capitalize()
        self.author: str = author.capitalize()
        self.pages: int = pages
        self.is_borrowed: bool = False
        self.borrower: str | None = None
        self.borrow_history: list[tuple[str, datetime]] = []
        self.archived: bool = False

    

    def borrow(self, user: str) -> None:
        if self.archived:
            raise Exception("kitob arxivlangan")
        
        if self.is_borrowed:
            raise Exception("kitob allqachon olingan")
        
        self.is_borrowed = True
        self.borrower = user

        self.borrow_history.append((user, datetime.now()))


    def return_book(self) -> None:
        if not self.is_borrowed:
            raise Exception("kitob ijaraga berilmagan")
        
        self.borrower = None
        self.is_borrowed = False


    def change_title(self, new_title: str) -> None:
        if not new_title:
            raise Exception("title bo'sh bo'lmasligi kerak")
        
        if self.archived:
            raise Exception("kitob arxivlangan")

        self.title = new_title


    def archive(self) -> None:
        if self.is_borrowed:
            raise Exception("kitob ijaraga berilgan")
        
        self.archived = True


    def info(self) -> dict:
        status = "available"
        if self.archived:
            status = "archived"
        elif self.borrower:
            status = "borrowed"

        return {
            "id": self.id,
            "title": self.title, 
            "author": self.author,
            "pages": self.pages,
            "status": status,
            "borrower": self.borrower,
            "times_borrowed": len(self.borrow_history) 
        }



    def __str__(self):
        return f"Book {self.title}"
    

    def __repr__(self):
        f"Book(id={self.id}, title={self.title}, borrowed={self.is_borrowed})"

    
    def __eq__(self, value):
        return self.id == value.id
    

    def __len__(book):
        return book.pages
    

    def __bool__(book):
        return False if book.archived else True


    @staticmethod
    def is_correct_item(id: int, title: str, author: str, pages: int) -> None:
        """
        Validate constructor arguments for creating an item.

        Checks that:
        - id is an integer
        - title is not empty
        - author is not empty
        - pages is greater than zero

        Args:
            id (int): Unique identifier of the item.
            title (str): Title of the item.
            author (str): Author name.
            pages (int): Number of pages.

        Raises:
            ValueError: If any argument is invalid.
        """

        if type(id) != int:
            raise ValueError("Id butun son bo'lishligi kerak")
        
        if not title:
            raise ValueError("title bo'sh bo'lmasligi kerak")
        
        if not author:
            raise ValueError("author bo'sh bo'sh bo'lmasligi kerak")
        
        if pages <= 0:
            raise ValueError("pages no'ldan katta bo'lishligi kerak")
