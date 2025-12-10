import os
import time
import sys

# --- Konfigurasi Warna untuk Termux ---
HIJAU = "\033[92m"
KUNING = "\033[93m"
MERAH = "\033[91m"
BIRU = "\033[96m"
RESET = "\033[0m"

# --- Fungsi Bantuan ---
def bersihkan_layar():
    os.system('clear')

def efek_ketik(teks, kecepatan=0.05):
    """Mensimulasikan efek typing (Bagian Typing)"""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()

def header():
    bersihkan_layar()
    print(f"{BIRU}========================================")
    print(f"   STRUKTUR CENDIKIAWAN STUDIOS APP")
    print(f"========================================{RESET}")

# --- BAGIAN A: INTRODUCE ---
def loading_screen():
    header()
    print(f"{KUNING}[A. Introduce - 1. Loading_start]{RESET}")
    time.sleep(1)
    print(f"{KUNING}[A. Introduce - 2. Loading_middle]{RESET}")
    time.sleep(1)
    print(f"{HIJAU}[A. Introduce - 3. Loading_done]{RESET}")
    time.sleep(1)
    print(f"\n{BIRU}[A. Introduce - 4. Welcome]{RESET}")
    efek_ketik("Selamat Datang di Super App Indonesia...", 0.05)
    time.sleep(1)

# --- BAGIAN B: LOGIN ---
def menu_login():
    header()
    print(f"{KUNING}--- [B. LOGIN PAGE] ---{RESET}")
    print("Status: [1. Login_empty]\n")
    
    # Input Username
    print("Silakan masukkan Username Anda.")
    username = input(f"{HIJAU}Username: {RESET}")
    
    if len(username) > 0:
        print(f"{KUNING}> System: [2. Login_typing] mendeteksi input...{RESET}")
        time.sleep(0.5)
    else:
        print(f"{MERAH}> Error: Masih kosong!{RESET}")
        time.sleep(1)
        return menu_login() # Ulangi

    # Input Password
    print("\nSilakan masukkan Password Anda.")
    password = input(f"{HIJAU}Password: {RESET}")

    if len(password) > 0:
        print(f"{KUNING}> System: [2. Login_typing] mendeteksi input...{RESET}")
        time.sleep(0.5)
        print(f"{HIJAU}> System: [3. Login_filled] Data terisi.{RESET}")
    
    # Simulasi Cek Login
    print("\nSedang memverifikasi...")
    time.sleep(1)
    
    if username == "admin" and password == "123":
        print(f"\n{HIJAU}LOGIN BERHASIL! Menuju Home...{RESET}")
        time.sleep(1)
        menu_home(username)
    else:
        print(f"\n{MERAH}LOGIN GAGAL! Username/Password salah.{RESET}")
        input("Tekan Enter untuk mencoba lagi...")
        menu_login()

# --- BAGIAN H: HOME ---
def menu_home(user):
    header()
    print(f"{HIJAU}--- [H. HOME - 1. Home] ---{RESET}")
    print(f"Halo, {user}! Anda berada di dashboard utama.")
    print(f"Lokasi: [I. Select Location - 1. My Location]")
    print("\nMenu Tersedia:")
    print("1. Foods [K01]")
    print("2. Drinks [K02]")
    print("3. Profile [Y]")
    print("4. Logout")
    
    pilihan = input(f"\n{BIRU}Pilih menu (1-4): {RESET}")
    
    if pilihan == '4':
        print("Logging out...")
        main()
    elif pilihan == '3':
        print(f"\n{KUNING}[Y. Profile] Menampilkan profil user...{RESET}")
        input("Tekan Enter kembali ke Home...")
        menu_home(user)
    else:
        print("\nFitur sedang dalam pengembangan...")
        time.sleep(1)
        menu_home(user)

# --- MAIN LOOP ---
def main():
    loading_screen()
    while True:
        header()
        print("Silakan pilih opsi:")
        print("1. Login (Masuk)")
        print("2. Signup (Daftar)")
        print("3. Exit (Keluar)")
        
        pilihan = input(f"\n{BIRU}Pilihan Anda >> {RESET}")
        
        if pilihan == "1":
            menu_login()
        elif pilihan == "2":
            print(f"\n{KUNING}[C. Signup] Fitur ini simulasi...{RESET}")
            efek_ketik("Masuk ke halaman pendaftaran...", 0.03)
            time.sleep(1)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan Cendikiawan App.")
            sys.exit()
        else:
            print("Pilihan tidak valid.")
            time.sleep(1)

if __name__ == "__main__":
    main()
