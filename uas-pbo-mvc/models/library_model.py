class LibraryModel:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def get_books(self):
        return self.books.values()

    def get_book(self, book_id):
        return self.books.get(book_id)

    def update_book(self, book_id, title, author):
        if book_id in self.books:
            self.books[book_id].title = title
            self.books[book_id].author = author

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

    def borrow_book(self, book_id):
        book = self.get_book(book_id)
        if book and book.status == "tersedia":
            book.status = "dipinjam"
            return True
        return False

    def return_book(self, book_id):
        book = self.get_book(book_id)
        if book and book.status == "dipinjam":
            book.status = "tersedia"
            return True
        return False