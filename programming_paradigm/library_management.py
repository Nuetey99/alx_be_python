class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    

    def check_out(self):
        self.is_checked_out = True


    def return_book(self):
        self.is_checked_out = False

    def is_available(self):
        return not self.is_checked_out
    

class Library:
    def __init__(self):
        self.books = []



    def Add_Book(self,book):
        self.books.append(book)

    def Check_Out_Book ( self , title ):
        for book in self.books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'")
            else:
                print(f"Book {title} has been checked out or does not exist.")

    
    def Return_Book ( self , title ):
        for book in self.books:
            if book.title == title and not book.is_available():
                book.return_book()
            else:
                print(f"Book '{title}' was not checked out or does not exist.")


    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if not available_books:
            print ("No books are currently available")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")