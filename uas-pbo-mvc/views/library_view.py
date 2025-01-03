class LibraryView:
    @staticmethod
    def display_books(books):
        if not books:
            print("Tidak ada buku di perpustakaan.")
        else:
            for book in books:
                print(book)

    @staticmethod
    def display_message(message):
        print(message)