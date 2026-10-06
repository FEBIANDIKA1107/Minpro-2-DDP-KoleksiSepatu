# Minpro 2 DDP - Koleksi Sepatu

**Nama:** Raisha Achdi Febiandika  
**NIM:** 2609116071  
**Kelas:** B

## 1. Deskripsi Program

Program ini merupakan pengembangan dari Mini Project 1 dengan tema **Sistem Pengelolaan Data Koleksi Sepatu**. Program dibuat menggunakan bahasa pemrograman Python untuk mengelola data koleksi sepatu yang terdiri dari merek, jenis/model, dan ukuran sepatu.

Pada Mini Project 2, program dikembangkan dengan menambahkan **Dictionary, Function, Login, dan sistem hak akses berdasarkan role**. Program memiliki dua role, yaitu **Admin** dan **User**. Admin memiliki akses untuk menambah, melihat, mengubah, dan menghapus data koleksi sepatu, sedangkan User hanya memiliki akses untuk melihat data.

Program juga dilengkapi dengan validasi input untuk menangani kesalahan masukan pengguna serta menggunakan library `datetime` untuk menampilkan waktu ketika data berhasil ditambahkan.

## 2. Flowchart Program

### 2.1 Flowchart
<img width="1210" height="1262" alt="FLOWCHRTMINPRO2 drawio" src="https://github.com/user-attachments/assets/307c2465-3731-45e9-b51f-515111738588" />

### 2.2 Penjelasan Flowchart
Program dimulai dengan proses inisialisasi data koleksi sepatu dan data akun pengguna. Setelah itu, pengguna diminta memasukkan username dan password pada halaman login.

Sistem melakukan pengecekan terhadap username dan password. Jika data login tidak benar, sistem menampilkan pesan kesalahan dan pengguna kembali ke proses login. Jika login berhasil, sistem melakukan pengecekan role pengguna.

Jika role yang digunakan adalah Admin, pengguna diarahkan ke Menu Admin. Admin dapat memilih menu Tambah Data, Lihat Data, Ubah Data, Hapus Data, atau Logout. Setelah proses Tambah, Lihat, Ubah, atau Hapus selesai, pengguna kembali ke Menu Admin. Jika memilih Logout, pengguna kembali ke halaman Login.

Jika role yang digunakan adalah User, pengguna diarahkan ke Menu User. User hanya dapat memilih menu Lihat Data atau Logout. Setelah melihat data, pengguna kembali ke Menu User. Jika memilih Logout, pengguna kembali ke halaman Login.

Apabila pengguna memasukkan pilihan menu yang tidak sesuai, sistem menampilkan pesan bahwa pilihan tidak valid dan pengguna kembali ke menu sesuai dengan role yang digunakan.

## 3. Program dan Dokumentasi Output

### 3.1 Login
<img width="656" height="58" alt="Cuplikan layar 2026-10-06 131638" src="https://github.com/user-attachments/assets/a52dc584-bb02-424e-a248-222d66d0d901" />
Program memiliki fitur login menggunakan username dan password. Terdapat dua role pengguna, yaitu Admin dan User. Sistem akan memeriksa username dan password yang dimasukkan sebelum memberikan akses ke menu sesuai dengan role pengguna.

### 3.2 Menu Admin
<img width="656" height="67" alt="Cuplikan layar 2026-10-06 131901" src="https://github.com/user-attachments/assets/099abcc2-4a07-4b3d-adba-347c988c95ac" />
Menu Admin menyediakan lima pilihan, yaitu Tambah Data, Lihat Data, Ubah Data, Hapus Data, dan Logout. Admin memiliki hak akses penuh untuk mengelola data koleksi sepatu.

### 3.3 Tambah Data
<img width="657" height="45" alt="Cuplikan layar 2026-10-06 132257" src="https://github.com/user-attachments/assets/891b7867-510a-4857-be48-e7116ba36bfa" />
Fitur Tambah Data digunakan untuk menambahkan koleksi sepatu baru. Pengguna memasukkan merek dan ukuran sepatu. Jenis/model sepatu akan ditentukan berdasarkan merek yang dipilih. Setelah data berhasil ditambahkan, program menampilkan waktu penambahan data.

### 3.4 Lihat Data
<img width="656" height="171" alt="Cuplikan layar 2026-10-06 132435" src="https://github.com/user-attachments/assets/f55a03e4-3ef6-4358-8317-55f77eefef0e" />
Fitur Lihat Data digunakan untuk menampilkan seluruh data koleksi sepatu yang telah tersimpan. Data ditampilkan berdasarkan nomor, merek, jenis, dan ukuran sepatu.

### 3.5 Ubah Data
<img width="653" height="46" alt="Cuplikan layar 2026-10-06 132625" src="https://github.com/user-attachments/assets/a6f3846f-6078-4cc2-b4f6-c6dbd312fd16" />
<img width="656" height="173" alt="Cuplikan layar 2026-10-06 132701" src="https://github.com/user-attachments/assets/e98b38c6-c94f-451a-8baf-563db0a66b17" />
Fitur Ubah Data digunakan untuk mengubah informasi koleksi sepatu yang telah tersimpan. Pengguna memilih nomor data, kemudian memasukkan merek dan ukuran baru. Program akan memperbarui data tersebut.

### 3.6 Hapus Data
<img width="656" height="26" alt="Cuplikan layar 2026-10-06 132944" src="https://github.com/user-attachments/assets/98e5ce98-b439-467d-825a-a27d6487054d" />
<img width="652" height="116" alt="Cuplikan layar 2026-10-06 133023" src="https://github.com/user-attachments/assets/d966eec7-0898-4aa0-a2b2-0bd1cfa85710" />
Fitur Hapus Data digunakan untuk menghapus data koleksi sepatu berdasarkan nomor data yang dipilih. Jika data tersedia, sistem akan menghapus data dan menampilkan pesan bahwa data berhasil dihapus.

### 3.7 Menu User
<img width="656" height="77" alt="Cuplikan layar 2026-10-06 133237" src="https://github.com/user-attachments/assets/64d2d6b3-ebcc-41ca-85da-75ba331f393c" />
Menu User memiliki hak akses yang berbeda dari Admin. User hanya dapat melihat data koleksi sepatu dan melakukan Logout. User tidak memiliki akses untuk menambah, mengubah, atau menghapus data.

### 3.8 Logout
<img width="654" height="17" alt="Cuplikan layar 2026-10-06 133355" src="https://github.com/user-attachments/assets/919809cb-8aeb-4efe-a377-02efcc9cd4e5" />
Fitur Logout digunakan untuk keluar dari menu Admin atau User dan kembali ke halaman Login. Dengan demikian, pengguna dapat melakukan login kembali menggunakan akun yang berbeda.

## 4. Nilai Tambah Program
