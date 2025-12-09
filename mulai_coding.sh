#!/bin/bash

# Warna
CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

clear
echo -e "${CYAN}==============================================${NC}"
echo -e "${CYAN}   🚀 DIEHANTAR DEV ENVIRONMENT (TERMUX)      ${NC}"
echo -e "${CYAN}==============================================${NC}"

# 1. Cek & Jalankan Database MariaDB
echo -e "${YELLOW}[1] Memeriksa Database MariaDB...${NC}"
if pgrep "mysqld" > /dev/null
then
    echo -e "${GREEN}    Database sudah berjalan. Aman.${NC}"
else
    echo -e "${RED}    Database mati. Menghidupkan sekarang...${NC}"
    mysqld_safe > /dev/null 2>&1 &
    sleep 3
    echo -e "${GREEN}    Database BERHASIL dihidupkan!${NC}"
fi

echo ""

# 2. Cek File Kunci
if [ -f "dieHantar_Project/private-key.pem" ]; then
    echo -e "${GREEN}[OK] Private Key ditemukan.${NC}"
else
    echo -e "${RED}[WARNING] File private-key.pem tidak ditemukan di folder dieHantar_Project!${NC}"
fi

echo ""
echo -e "${YELLOW}[2] Menjalankan Bot Auto-Push...${NC}"
echo -e "    Tekan ${RED}CTRL + C${NC} untuk berhenti coding."
echo ""

# 3. Jalankan Bot Python
cd ~/dieHantar_Project
python bot_manager.py
