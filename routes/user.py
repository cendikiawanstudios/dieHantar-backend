nano app.py


http://googleusercontent.com/immersive_entry_chip/1

### 2. Update Database untuk Profil & Lokasi

Anda perlu menambahkan tabel untuk menyimpan lokasi, PIN, dan status Touch ID, sesuai dengan fitur (E, F, G, I).

**Akses MySQL**
```bash
mysql -u root -p
*(Masukkan password jika ada).*

**Jalankan Perintah SQL**
```sql
USE diehantar_db;

-- Tabel untuk menyimpan Lokasi Favorit/Tersimpan Pengguna (I. Select Location)
CREATE TABLE user_locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    label VARCHAR(100) NOT NULL, -- Contoh: 'Home', 'Office'
    address_detail TEXT NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    is_favorite BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tambahkan kolom keamanan ke tabel users yang sudah ada
-- Ini mendukung fitur E, F, G (PIN/Touch ID)
ALTER TABLE users
ADD COLUMN touch_id_enabled BOOLEAN DEFAULT FALSE,
ADD COLUMN pin_security_hash VARCHAR(255) NULL,
ADD COLUMN profile_picture VARCHAR(255) NULL;

EXIT;

## 🚀 Ringkasan dan Tindakan

1.  **Jalankan Perintah SQL** untuk membuat `user_locations` dan mengubah tabel `users`.
2.  **Buat File `routes/user.py`** dan masukkan kode di atas.
3.  **Perbarui `app.py`** untuk mendaftarkan `user_bp`.
4.  **Restart Server Flask** (`Ctrl + C` lalu `python app.py`).

Setelah ini, *backend* Anda akan dapat menangani hampir semua fungsionalitas inti Super App, dari otentikasi hingga pemesanan dan manajemen profil!

Apakah Anda ingin melanjutkan dengan menguji *endpoint* `routes/user.py` ini atau Anda ingin fokus pada fitur lain seperti **Promotions (P)** atau **Notification (X)**?
