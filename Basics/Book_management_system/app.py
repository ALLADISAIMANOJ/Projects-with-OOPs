from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
    
    @abstractmethod
    def borrow_book(self, library, book_id):
        pass
    
    @abstractmethod
    def return_book(self, library, book_id):
        pass

class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.borrow_limit = 3
        self.borrow_duration = 14 # days
    
    def borrow_book(self, library, book_id):
        if len(library.borrowed_books.get(self.user_id,[])) >= self.borrow_limit:
            print(f"{self.name} has reached the borrowing limit.")
            return False
        return library.borrow_book(self.user_id, book_id, self.borrow_duration)
    
    def return_book(self, library, book_id):
        return library.return_book(self.user_id, book_id)

class Professor(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.borrow_limit = 5
        self.borrow_duration = 28 # days
    
    def borrow_book(self, library, book_id):
        if len(library.borrowed_books.get(self.user_id,[])) >= self.borrow_limit:
            print(f"{self.name} has reached the borrowing limit.")
            return False
        return library.borrow_book(self.user_id, book_id, self.borrow_duration)
    
    def return_book(self, library, book_id):
        return library.return_book(self.user_id, book_id)

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.borrower_id = None
        self.due_date = None

class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {} # {user_id: [book_id1, book_id2, ...]}
    
    def add_book(self, book):
        self.books[book.book_id] = book
    
    def borrow_book(self, user_id, book_id, duration):
        if book_id not in self.books:
            print("Book not found in the library.")
            return False
        
        book = self.books[book_id]
        if not book.is_available:
            print(f"Book '{book.title}' is currently unavailable.")
            return False
        
        book.is_available = False
        book.borrower_id = user_id
        book.due_date = datetime.now() + timedelta(days=duration)
        
        if user_id not in self.borrowed_books:
            self.borrowed_books[user_id] = []
        self.borrowed_books[user_id].append(book_id)
        
        print(f"Book '{book.title}' borrowed by user ID {user_id} until {book.due_date}.")
        return True
    
    def return_book(self, user_id, book_id):
        if user_id not in self.borrowed_books or book_id not in self.borrowed_books[user_id]:
            print("This book was not borrowed by this user.")
            return False
        
        book = self.books[book_id]
        book.is_available = True
        book.borrower_id = None
        book.due_date = None
        
        self.borrowed_books[user_id].remove(book_id)
        
        print(f"Book '{book.title}' returned by user ID {user_id}.")
        return True
    
    def check_availability(self, book_id):
        if book_id in self.books:
            return self.books[book_id].is_available
        return False

# Example Usage
if __name__ == "__main__":
    library = Library()
    
    book1 = Book(1, "1984", "George Orwell")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee")
    book3 = Book(3, "The Great Gatsby", "F. Scott Fitzgerald")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    student = Student(101, "Alice")
    professor = Professor(201, "Dr. Smith")
    
    student.borrow_book(library, 1)
    student.borrow_book(library, 2)
    student.return_book(library, 1)
    
    professor.borrow_book(library, 1)
    professor.borrow_book(library, 2)
    professor.borrow_book(library, 3)
