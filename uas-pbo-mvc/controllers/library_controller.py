from models.book_model import Book
from models.library_model import LibraryModel
from views.library_view import LibraryView

class LibraryController:
    def __init__(self):
        self.model = LibraryModel()
        self.view = LibraryView()

    def add_book(self, book_id, title, author):
        if self.model.get_book(book_id):
            self.view.display_message("Buku dengan ID tersebut sudah ada.")
        else:
            book = Book(book_id, title, author)
            self.model.add_book(book)
            self.view.display_message("Buku berhasil ditambahkan.")

    def display_books(self):
        books = self.model.get_books()
        self.view.display_books(books)

    def edit_book(self, book_id, title, author):
        if self.model.get_book(book_id):
            self.model.update_book(book_id, title, author)
            self.view.display_message("Informasi buku berhasil diperbarui.")
        else:
            self.view.display_message("Buku tidak ditemukan.")

    def delete_book(self, book_id):
        if self.model.get_book(book_id):
            self.model.delete_book(book_id)
            self.view.display_message("Buku berhasil dihapus.")
        else:
            self.view.display_message("Buku tidak ditemukan.")

    def borrow_book(self, book_id):
        if self.model.borrow_book(book_id):
            self.view.display_message("Buku berhasil dipinjam.")
        else:
            self.view.display_message("Buku tidak tersedia atau sedang dipinjam.")

    def return_book(self, book_id):
        if self.model.return_book(book_id):
            self.view.display_message("Buku berhasil dikembalikan.")
        else:
            self.view.display_message("Buku tidak ditemukan atau belum dipinjam.")
