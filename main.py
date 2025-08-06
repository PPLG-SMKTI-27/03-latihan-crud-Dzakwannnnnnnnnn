# data buku

from tabulate import tabulate
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
] 

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def tampilkan_data():
    print(tabulate(books, headers="keys" , tablefmt="grid"))

def tambah_data():
    print("Menambahkan Data")
    isbn = input("Isi ISBN: ")
    judul = input("Masukan Judul: ")
    pengarang = input("Masukan nama pengarang: ")
    jumlah = input("Masukan jumlah buku: ")
    terpinjam = input("Masukan buku yang terpinjam: ")
    book = {"isbn":isbn, "judul":judul, "pengarang":pengarang, "jumlah":jumlah, "terpinjam": 0}
    books.append(book)

def edit_data():
    index = int(input("Masukan data yang akan baru: "))
    books[index]["isbn"] = input("Masukan isbn yang baru: ")
    books[index]["judul"] = input("Masukan judul buku yang baru: ")
    books[index]["pengarang"] = input("Masukan nama pengarang yang baru: ")
    books[index]["jumlah"] = input("Masukan jumlah buku: ")
    books[index]["terpinjam"] = input("Masukan buku yang terpinjam: ")
    print("Data buku telah di update!")


def hapus_data():
    index = int(input("Masukan index data buku yang ingin dihapus: "))
    books.pop(index)

    print("Buku berhasil dihapus")

def tampilkan_peminjaman():
    print(tabulate(records, headers="keys" , tablefmt="grid"))

def tampilkan_belum():
    print("======Buku yang belum kembali======")
    print(tabulate([records for records in records if["tanggal_kembali"] is None], headers="keys" , tablefmt="grid"))

def peminjaman():
    tampilkan_data()
    isbn = input("Masukan isbn buku yang ingin dipinjam: ")
    nama = input("Masukan nama peminjam: ")
    tanggal_pinjam = input("Masukan tanggal pinjam (YYYY-MM-DD): ")
    for book in books:
        if book["isbn"] == isbn:
            if book["jumlah"] > book["terpinjam"]:
                book["jumlah"] -= 1
                book["terpinjam"] += 1
                records.append({"isbn": isbn, "nama": nama, "status": "belum", "tanggal_pinjam": tanggal_pinjam, "tanggal_kembali": None})
                print("Buku telah dipinjam")
                tampilkan_peminjaman()
                return
            else:
                print("Buku dengan isbn belum")
                return
def pengembalian():
    tampilkan_data()
    isbn = input("Masukan isbn buku yang ingin dikembalikan: ")
    nama = input("Masukan nama peminjam: ")
    tanggal_pinjam = input("Masukan tanggal pinjam (YYYY-MM-DD): ")
    for book in books:
        if book["isbn"] == isbn:
            for record in records:
                if record["isbn"] == isbn and record["tanggal_kembali"] is None:
                    book["jumlah"] -= 1
                    book["terpinjam"] += 1
                    record["tanggal_kembali"] = input("Masukan tanggal kembali (YYYY-MM-DD): ")
                    record["status"] = "Selesai"
                    print("Buku telah dikembalikan.")
                    tampilkan_peminjaman()
                    return
                print("Buku ini belum dipinjam atau sudah dikembalikan.")
                return
        print("Buku dengan isbn tersebut tidak ditemukan")

while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    
    match menu:
        case "1":
            tampilkan_data()
            input("Enter Untuk Melanjutkan")
        case "2":
            tambah_data()
            input("Enter Untuk Melanjutkan")
        case "3":
            edit_data()
            input("Enter Untuk Melanjutkan")
        case "4":
            hapus_data()
            input("Enter Untuk Melanjutkan")
        case "5":
            tampilkan_peminjaman()
            input("Enter Untuk Melanjutkan")
        case "6":
            tampilkan_belum()
            input("Enter Untuk Melanjutkan")
        case "7":
            peminjaman()
            input("Enter Untuk Melanjutkan")
        case "8":
            pengembalian()
            input("Enter Untuk Melanjutkan")
        case "x":
            exit()
        case _ :
            print ("input harus  bilangan (1-4) atau (x) untuk keluar")