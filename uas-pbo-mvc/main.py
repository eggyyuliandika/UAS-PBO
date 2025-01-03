from controllers.library_controller import LibraryController

if __name__ == "__main__":
    controller = LibraryController()

    while True:
        print("\n==========Fitur Perpustakaan==========")
        print("1. Tambah Buku")
        print("2. Tampilkan Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("5. Pinjam Buku")
        print("6. Kembalikan Buku")
        print("7. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            book_id = input("Masukkan ID Buku: ")
            title = input("Masukkan Judul Buku: ")
            author = input("Masukkan Penulis Buku: ")
            controller.add_book(book_id, title, author)
        elif choice == "2":
            controller.display_books()
        elif choice == "3":
            book_id = input("Masukkan ID Buku yang ingin diedit: ")
            title = input("Masukkan Judul Buku Baru: ")
            author = input("Masukkan Penulis Buku Baru: ")
            controller.edit_book(book_id, title, author)
        elif choice == "4":
            book_id = input("Masukkan ID Buku yang ingin dihapus: ")
            controller.delete_book(book_id)
        elif choice == "5":
            book_id = input("Masukkan ID Buku yang ingin dipinjam: ")
            controller.borrow_book(book_id)
        elif choice == "6":
            book_id = input("Masukkan ID Buku yang ingin dikembalikan: ")
            controller.return_book(book_id)
        elif choice == "7":
            print("Terima kasih telah menggunakan aplikasi perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
