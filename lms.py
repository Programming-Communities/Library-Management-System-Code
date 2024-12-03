# Library Management System

# Data Structures
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"},
    {"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "status": "Available"},
]

users = [
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": []},
]

# Functions

def view_books(status=None):
    """Display books based on status (All, Available, Checked Out)"""
    print("\nAll Books:")
    for book in books:
        if status is None or book["status"] == status:
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')

def search_books(keyword, search_type):
    """Search books by title, author, or genre"""
    print("\nSearch Results:")
    for book in books:
        if keyword.lower() in book[search_type].lower():
            print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')

def borrow_book(user_id, book_id):
    """Allow user to borrow a book if available"""
    user = next((u for u in users if u["id"] == user_id), None)
    book = next((b for b in books if b["id"] == book_id), None)
    
    if not user:
        print("\nInvalid User ID.")
        return
    if not book:
        print("\nInvalid Book ID.")
        return
    if book["status"] == "Checked Out":
        print(f'\nSorry, the book "{book["title"]}" is currently checked out.')
    else:
        book["status"] = "Checked Out"
        user["borrowed_books"].append(book["title"])
        print(f'\nYou have successfully borrowed "{book["title"]}".')

def return_book(user_id, book_id):
    """Allow user to return a book"""
    user = next((u for u in users if u["id"] == user_id), None)
    book = next((b for b in books if b["id"] == book_id), None)
    
    if not user:
        print("\nInvalid User ID.")
        return
    if not book:
        print("\nInvalid Book ID.")
        return
    if book["title"] not in user["borrowed_books"]:
        print(f'\nYou have not borrowed the book "{book["title"]}".')
    else:
        book["status"] = "Available"
        user["borrowed_books"].remove(book["title"])
        print(f'\nYou have successfully returned "{book["title"]}".')

def view_users():
    """Display all users and their borrowed books"""
    print("\nUsers and Borrowed Books:")
    for user in users:
        borrowed = ", ".join(user["borrowed_books"]) if user["borrowed_books"] else "None"
        print(f'{user["id"]}. {user["name"]} - Borrowed Books: {borrowed}')

# Main Menu
def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            view_books()
        elif choice == "2":
            keyword = input("\nEnter keyword to search: ")
            search_type = input("Search by (title/author/genre): ").strip().lower()
            if search_type in ["title", "author", "genre"]:
                search_books(keyword, search_type)
            else:
                print("\nInvalid search type. Please choose title, author, or genre.")
        elif choice == "3":
            try:
                user_id = int(input("\nEnter your User ID: "))
                book_id = int(input("Enter the Book ID you want to borrow: "))
                borrow_book(user_id, book_id)
            except ValueError:
                print("\nInvalid input. User ID and Book ID must be numbers.")
        elif choice == "4":
            try:
                user_id = int(input("\nEnter your User ID: "))
                book_id = int(input("Enter the Book ID you want to return: "))
                return_book(user_id, book_id)
            except ValueError:
                print("\nInvalid input. User ID and Book ID must be numbers.")
        elif choice == "5":
            view_users()
        elif choice == "6":
            print("\nThank you for using the Library Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
