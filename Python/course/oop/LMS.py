class Book:
    def __init__(self,title, author, total_copies):
        self.title = title
        self.author = author
        self.__total_copies = total_copies
        self.__borrowed_copies = 0
    
    def display_info(self):
        print(f"--------Book Info-------")
        print(f"\tTitle: {self.title}")
        print(f"\tAuthor: {self.author}")
        print(f"\tTotal Copies: {self.__total_copies}")
        print(f"\tBorrowed Copies: {self.__borrowed_copies}")
        print(f"\tAvailable Copies: {self.available()}")
    def borrow_book(self):
        if self.__borrowed_copies < self.__total_copies:
            self.__borrowed_copies+=1
            print(f"Borrowed 1 copy of {self.title}")
        else:
            print(f"Sorry, all copies of {self.title} are currently borrowed.")
    def return_book(self):
        if self.__borrowed_copies >0:
            self.__borrowed_copies-=1
            print(f"Returned 1 copy of {self.title}")   
        else:
            print(f"No copies of {self.title} are borrowed.")    
    
    def available(self):
        return self.__total_copies - self.__borrowed_copies
        
book = Book("Alissa", "C.J Moore", 5)
book.display_info()
book.borrow_book()
# book.__total_copies = 10
book.borrow_book()
book.borrow_book()
book.borrow_book()
# book.__borrowed_copies= 100
book.display_info()
book.return_book()
book.display_info()