nano app.py


http://googleusercontent.com/immersive_entry_chip/1

---

## 📝 2. Skema Database Awal (dieHantar-myserver)

Berdasarkan struktur proyek Anda, terutama bagian **Login/Signup (B, C, D)** dan **Foods/Drinks/Services (K, L, M, N)**, Anda membutuhkan setidaknya tiga tabel utama:

### Tabel 1: `users` (Untuk B. Login & C. Signup)

| Kolom | Tipe Data | Deskripsi | Keterangan
| :--- | :--- | :--- | :---
| `id` | INT (PK) | ID unik pengguna |
| `nama` | VARCHAR(255) | Nama lengkap pengguna |
| `email` | VARCHAR(255) | Email (Harus unik) | Untuk login
| `phone_number` | VARCHAR(15) | Nomor telepon (Harus unik) | Untuk verifikasi OTP
| `password_hash` | VARCHAR(255) | Hash kata sandi | Untuk keamanan
| `is_verified` | BOOLEAN | Status verifikasi OTP/Email | Sesuai D. Otp code verification
| `created_at` | DATETIME | Waktu pendaftaran |

### Tabel 2: `products` (Tabel Induk untuk Menu)

Tabel ini akan menyimpan daftar item (makanan/minuman) yang dijual.

| Kolom | Tipe Data | Deskripsi | Keterangan
| :--- | :--- | :--- | :---
| `id` | INT (PK) | ID unik item |
| `nama` | VARCHAR(255) | Nama Menu |
| `deskripsi` | TEXT | Deskripsi item |
| `harga` | INT | Harga jual |
| `kategori` | ENUM | Kategori: `FOOD`, `DRINK`, `SERVICE` | Sesuai K01, K02, K03
| `restoran_id` | INT (FK) | ID restoran/vendor |

### Tabel 3: `orders` (Untuk O. My Basket & Q. Order Tracking)

| Kolom | Tipe Data | Deskripsi | Keterangan
| :--- | :--- | :--- | :---
| `id` | INT (PK) | ID unik pesanan |
| `user_id` | INT (FK) | Pengguna yang memesan |
| `driver_id` | INT (FK) | Driver yang menerima pesanan | R. Driver information
| `status` | ENUM | Status pesanan | Q. Order Tracking
| `total_harga` | INT | Total akhir pesanan |
| `alamat_kirim` | TEXT | Detail alamat pengiriman | I. Select Location
| `created_at` | DATETIME | Waktu pesanan dibuat |

---

## 💡 Langkah Selanjutnya

1.  **Lakukan *Commit* Git:** Setelah perubahan di `app.py` dan `routes/menu.py` ini, jalankan `git add .`, `git commit -m "Refactor: Add routes folder and menu blueprint"`, dan `git push -u origin main` (gunakan PAT yang baru, valid, dan berizin `repo`).
2.  **Uji Server Baru:** Aktifkan `venv` dan jalankan `python app.py`. Uji *endpoint* baru Anda: `http://10.93.105.91:8000/api/v1/menu/makanan`.
3.  **Implementasi Login/Signup:** Selanjutnya, kita bisa fokus membuat *endpoint* di `routes/auth.py` untuk menangani fitur B, C, dan D, menggunakan tabel `users`.

Apakah Anda ingin fokus membuat *endpoint* **registrasi pengguna** di `routes/auth.py`?
