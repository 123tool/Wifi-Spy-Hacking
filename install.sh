#!/bin/bash

# -------------------------------------------------------------------------
# Installer for Wifi SpyE
# Dev : 123tool & SPY-E
# -------------------------------------------------------------------------

# Warna untuk output
CYAN='\033[0;36m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}====================================================${NC}"
echo -e "${CYAN}       WIFI SPYE - AUTO INSTALLER                   ${NC}"
echo -e "${CYAN}       By: 123tool & SPY-E                          ${NC}"
echo -e "${CYAN}====================================================${NC}"

# Cek apakah user menjalankan sebagai root
if [ "$EUID" -ne 0 ]; then 
  echo -e "${RED}[!] Harap jalankan script ini dengan sudo!${NC}"
  exit
fi

echo -e "${GREEN}[+] Memperbarui repositori...${NC}"
apt-get update -y

echo -e "${GREEN}[+] Menginstal Python dan Pip...${NC}"
apt-get install python3 python3-pip git -y

echo -e "${GREEN}[+] Menginstal Library Python (Colorama)...${NC}"
pip3 install colorama --break-system-packages 2>/dev/null || pip3 install colorama

echo -e "${GREEN}[+] Menginstal Tools Audit Jaringan (Ini mungkin memakan waktu)...${NC}"
# Daftar tools esensial
apt-get install -y aircrack-ng nmap crunch reaver pixiewps bully wifite wifiphisher nikto netcat-traditional gobuster sqlmap

echo -e "${GREEN}[+] Memberikan izin eksekusi pada script utama...${NC}"
chmod +x wifi_spye.py

echo -e "${CYAN}====================================================${NC}"
echo -e "${GREEN}  INSTALASI SELESAI!${NC}"
echo -e "${WHITE}  Untuk menjalankan, ketik: ${CYAN}sudo python3 wifi_spye.py${NC}"
echo -e "${CYAN}====================================================${NC}"
