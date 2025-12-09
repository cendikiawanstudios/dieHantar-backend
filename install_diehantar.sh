#!/bin/bash

# Warna untuk output text agar lebih mudah dibaca
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

clear
echo -e "${CYAN}====================================================${NC}"
echo -e "${CYAN}    AUTOMATIC INSTALLER FOR DIEHANTAR (TERMUX)      ${NC}"
echo -e "${CYAN}====================================================${NC}"
echo ""

# 1. Update dan Upgrade Termux
echo -e "${YELLOW}[1/5] Memperbarui paket Termux...${NC}"
pkg update -y && pkg upgrade -y

# 2. Install Dependensi (Git, Node.js, MariaDB)
echo -e "${YELLOW}[2/5] Menginstall Git, Node.js, dan MariaDB...${NC}"
pkg install git nodejs mariadb -y

# Cek apakah instalasi berhasil
if ! command -v git &> /dev/null; then
    echo -e "${RED}Gagal menginstall Git. Silakan cek koneksi internet.${NC}"
    exit 1
fi

# Buat folder utama proyek
PROJECT_DIR="$HOME/dieHantar_Project"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

echo -e "${GREEN}Folder proyek dibuat di: $PROJECT_DIR${NC}"
echo ""

# 3. Clone & Setup Frontend
echo -e "${YELLOW}[3/5] Mengunduh Frontend (dieHantar-frontend)...${NC}"
if [ -d "dieHantar-frontend" ]; then
    echo -e "${RED}Folder dieHantar-frontend sudah ada. Melewati clone.${NC}"
else
    git clone https://github.com/cendikiawanstudios/dieHantar-frontend
fi

# Masuk dan install node_modules jika ada package.json
if [ -d "dieHantar-frontend" ]; then
    echo -e "      Menginstall dependensi Frontend (npm install)..."
    cd dieHantar-frontend
    if [ -f "package.json" ]; then
        npm install
    else
        echo -e "${RED}      Tidak ditemukan package.json di frontend.${NC}"
    fi
    cd ..
fi
echo ""

# 4. Clone & Setup Backend
echo -e "${YELLOW}[4/5] Mengunduh Backend (dieHantar-backend)...${NC}"
if [ -d "dieHantar-backend" ]; then
    echo -e "${RED}Folder dieHantar-backend sudah ada. Melewati clone.${NC}"
else
    git clone https://github.com/cendikiawanstudios/dieHantar-backend
fi

# Masuk dan install node_modules jika ada package.json
if [ -d "dieHantar-backend" ]; then
    echo -e "      Menginstall dependensi Backend (npm install)..."
    cd dieHantar-backend
    if [ -f "package.json" ]; then
        npm install
    else
        echo -e "${RED}      Tidak ditemukan package.json di backend.${NC}"
    fi
    cd ..
fi
echo ""

# 5. Clone MyServer/Database
echo -e "${YELLOW}[5/5] Mengunduh Database/Server (dieHantar-myserver)...${NC}"
if [ -d "dieHantar-myserver" ]; then
    echo -e "${RED}Folder dieHantar-myserver sudah ada. Melewati clone.${NC}"
else
    git clone https://github.com/cendikiawanstudios/dieHantar-myserver
fi

echo ""
echo -e "${CYAN}====================================================${NC}"
echo -e "${GREEN}             INSTALASI SELESAI!                     ${NC}"
echo -e "${CYAN}====================================================${NC}"
echo ""
echo -e "Lokasi File: $PROJECT_DIR"
echo ""
echo -e "${YELLOW}Langkah Selanjutnya (PENTING):${NC}"
echo "1. Jalankan Database MariaDB:"
echo "   Ketik: mysqld_safe &"
echo ""
echo "2. Konfigurasi Backend & Frontend:"
echo "   Masuk ke masing-masing folder dan cek file .env atau config."
echo "   Pastikan port dan kredensial database sesuai."
echo ""
echo "3. Import Database:"
echo "   Cek folder 'dieHantar-myserver' untuk file .sql jika ada,"
echo "   lalu import ke MariaDB."
echo ""
