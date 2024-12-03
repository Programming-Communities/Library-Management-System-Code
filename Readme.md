
---

### 1. **Storing Books and Users**
The system has two lists: one for books and another for users.

**Books:**
- A list of dictionaries where each dictionary stores details about a book (ID, title, author, genre, and status).
- Example:
  ```python
  books = [
      {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"}
  ]
  ```

**Users:**
- A list of dictionaries where each dictionary stores details about a user (ID, name, and books they borrowed).
- Example:
  ```python
  users = [
      {"id": 1, "name": "Alice", "borrowed_books": []}
  ]
  ```

---

### 2. **Viewing Books**
The `view_books` function shows a list of all books. You can also filter to show only available books or only checked-out books.

- It goes through each book in the `books` list and prints details like title, author, and status.
- Example of how it works:
  ```python
  def view_books(status=None):
      for book in books:
          if status is None or book["status"] == status:
              print(f'{book["id"]}. "{book["title"]}" by {book["author"]} ({book["status"]})')
  ```

- If no status is provided, it shows all books. If you want only "Available" books, it shows just those.

---

### 3. **Borrowing Books**
The `borrow_book` function allows a user to borrow a book.

- It finds the user and book using their IDs.
- If the book is already checked out, it says, "Sorry, the book is currently checked out."
- If available, it marks the book as "Checked Out" and adds the book's title to the user's list of borrowed books.

Example of borrowing:
```python
borrow_book(1, 1)  # User ID 1 borrows Book ID 1.
```
---

### 4. **Returning Books**
The `return_book` function lets a user return a book.

- It finds the user and book using their IDs.
- If the user has borrowed the book, it marks the book as "Available" and removes it from the user's borrowed list.
- If the user hasn’t borrowed the book, it says, "You have not borrowed this book."

Example:
```python
return_book(1, 1)  # User ID 1 returns Book ID 1.
```

---

### 5. **Searching for Books**
The `search_books` function helps you find books by title, author, or genre.

- You provide a keyword (e.g., "Harper") and specify what to search (e.g., "author").
- The function looks for the keyword in the specified field and shows all matching books.

Example:
```python
search_books("Harper", "author")
```

---

### 6. **Viewing Users**
The `view_users` function shows all users and the books they’ve borrowed.

- Example:
  ```python
  view_users()
  ```
  It prints:
  ```
  1. Alice - Borrowed Books: None
  2. Bob - Borrowed Books: None
  ```

---

### 7. **Main Menu**
The `main_menu` function is like a big control room for the program.

- It shows options like viewing books, searching for books, borrowing or returning a book, viewing users, or exiting.
- Example menu:
  ```
  1. View all books
  2. Search for a book
  3. Borrow a book
  4. Return a book
  5. View all users
  6. Exit
  ```

You type a number (1–6) to choose an action.

---

### How It Works (Example Walkthrough)
1. Start the program.
2. It asks you to choose an option.
   - If you press `1`, it shows all books.
   - If you press `3`, it asks for your user ID and the book ID you want to borrow.
3. It keeps running until you press `6` to exit.

---
