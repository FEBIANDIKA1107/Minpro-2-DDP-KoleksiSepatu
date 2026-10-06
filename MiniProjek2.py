from datetime import datetime

data_sepatu = []

akun = {
    "admin" : {
        "password" : "admin123",
        "role" : "admin"
    },
    "user" : {
        "password" : "user123",
        "role" : "user"
    }
}

def login():
    while True:
        print("===== LOGIN =====")
        username = input("Username: ")
        password = input("Password: ")

        if username in akun:
            if password == akun[username]["password"]:
                print("Login berhasil.")
                return akun[username]["role"]
            else:
                print("Password salah")
        else:
            print("Username tidak ditemukan")

def menu_admin():
    while True:
        print("===== MENU ADMIN =====")
        print("1. Tambah Data")
        print("2. Lihat Data")
        print("3. Ubah Data")
        print("4. Hapus Data")
        print("5. Logout")

        pilihan = input("Masukkan pilihan menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("Logout berhasil.")
            return
        else:
            print("Pilihan tidak valid, silakan pilih 1-5.")

def tambah_data():
    while True:
        merek = input("Masukkan merek sepatu (Asics/Adidas/Nike/Puma/Ortuseight): ")

        if merek == "Asics":
            jenis = "Novablast"
            break
        elif merek == "Adidas":
            jenis = "Evo SL"
            break
        elif merek == "Nike":
            jenis = "Vaporfly"
            break
        elif merek == "Puma":
            jenis = "Fast Nitro"
            break
        elif merek == "Ortuseight":
            jenis = "Hyperblast"
            break
        else:
            print("Merek tidak tersedia, silakan masukkan kembali")

    while True:
        ukuran = input("Masukkan ukuran sepatu: ")

        if ukuran == "":
            print("Ukuran tidak boleh kosong.")
        else:
            break

    data_sepatu.append([merek, jenis, ukuran])

    waktu = datetime.now()
    print("Data berhasil ditambahkan.")
    print("waktu:", waktu)

def lihat_data():
    if data_sepatu == []:
        print("Data belum tersedia.")
    else:
        print("===== DATA KOLEKSI SEPATU =====")
        nomor = 1
        
        for data in data_sepatu:
            print("Data", nomor)
            print("Merek:", data[0])
            print("Jenis:", data[1])
            print("Ukuran:", data[2])
            print()
            nomor = nomor + 1

def ubah_data():
    if data_sepatu == []:
        print("Data belum tersedia.")
    else:
        while True:
            nomor = input("Masukkan nomor data yang ingin diubah: ")

            if nomor == "1" or nomor == "2" or nomor == "3" or nomor == "4" or nomor == "5":
                break
            else:
                print("Nomor data tidak valid.")

        if nomor == "1":
            indeks = 0
        elif nomor == "2":
            indeks = 1
        elif nomor == "3":
            indeks = 2
        elif nomor == "4":
            indeks = 3
        elif nomor == "5":
            indeks = 4

        if indeks >= len(data_sepatu):
            print("Data tidak ditemukan")
            return
        
        while True:
                merek = input("Masukkan merek baru (Asics/Adidas/Nike/Puma/Ortuseight): ")

                if merek == "Asics":
                    jenis = "Novablast"
                    break
                elif merek == "Adidas":
                    jenis = "Evo SL"
                    break
                elif merek == "Nike":
                    jenis = "Vaporfly"
                    break
                elif merek == "Puma":
                    jenis = "Fast Nitro"
                    break
                elif merek == "Ortuseight":
                    jenis = "Hyperblast"
                    break
                else:
                    print("Merek tidak tersedia, silakan masukkan kembali. ")

        while True:
                ukuran = input("Masukkan ukuran baru: ")

                if ukuran == "":
                    print("Ukuran tidak boleh kosong.")
                else:
                    break

        data_sepatu[indeks] = [merek, jenis, ukuran]
        print("Data berhasil diubah.")

def hapus_data():
    if data_sepatu == []:
        print("Data belum tersedia.")
    else:
        while True:
            nomor = input("Masukkan nomor data yang ingin dihapus: ")

            if nomor == "1" or nomor == "2" or nomor == "3" or nomor == "4" or nomor == "5":
                break   
            else:
                print("Nomor data tidak valid.")

        if nomor == "1":
            indeks = 0
        elif nomor == "2":
            indeks = 1
        elif nomor == "3":
            indeks = 2
        elif nomor == "4":
            indeks = 3
        elif nomor == "5":
            indeks = 4
            
        if indeks >= len(data_sepatu):
            print("Data tidak ditemukan")
            return

        del data_sepatu[indeks]
        print("Data berhasil dihapus.")

def menu_user():
    while True:
        print("===== MENU USER =====")
        print("1. Lihat Data")
        print("2. Logout")

        pilihan = input("Masukkan pilihan menu: ")

        if pilihan == "1":
            lihat_data()
        elif pilihan == "2":
            print("Logout berhasil.")
            return
        else:
            print("Pilihan tidak valid, silakan pilih 1-2.")

while True:
    role = login()

    if role == "admin":
        menu_admin()
    elif role == "user":
        menu_user()

