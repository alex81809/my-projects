class Library: 
    # to initialize the library with a list of books
    def __init__(self, books_list):
        self.books = books_list
        self.lended_books = {}
    
    # to display available books
    def display_books(self): 
        print("\n Available Books: ")
        for book in self.books: 
            print(f" = {book}")
        print()
    
    # to lend a book to a user
    def lend_book(self, book_name, user): 
        if book_name in self.books: 
            if book_name not in self.lended_books: 
                self.lended_books[book_name] = user
                print(f"\n '{book_name}' has been lent to {user}.")
            else: 
                print(f"\n Sorry, '{book_name}' is already lent to {self.lended_books[book_name]}.")
        else: 
            print("\n This book is not available in the library.")
        
    # to add a book 
    def add_book(self, book_name): 
        self.books.append(book_name)
        print(f"\n '{book_name}' has been added to the library.")
    
    # to return a book 
    def return_book(self, book_name): 
        if book_name in self.lended_books: 
            del self.lended_books[book_name]
            print(f"\n '{book_name}' has been returned successfully.")
        else: 
            print("\n This book was not lent from the library.")

# Creating the Library object
my_library = Library(["Harry Potter", "Python Basics", "Data Structures", "Rich Dad Poor Dad"])

# Menu-driven program
while True: 
    print("\n ===== Library Menu =====")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1': 
        my_library.display_books()
    elif choice == '2':
        book = input("Enter the name of the book you want to borrow: ")
        user = input("Enter your name: ")
        my_library.lend_book(book, user)
    elif choice == '3':
        book = input("Enter the name of the book to add: ")
        my_library.add_book(book)
    elif choice == '4': 
        book = input("Enter the name of the book you want to return: ")
        my_library.return_book(book)
    elif choice == '5':
        print("\n Exiting Library System. Thank you!")
        break
    else: 
        print("\n Invalid choice! Please pick a number from 1 to 5.")
