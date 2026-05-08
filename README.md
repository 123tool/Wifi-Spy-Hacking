# 📡 Wifi SpyE v2.0
**Advanced Wireless & Network Auditing Suite**

Wifi SpyE adalah framework sederhana berbasis Python yang menggabungkan berbagai tools keamanan jaringan populer ke dalam satu antarmuka yang mudah digunakan. Dibuat untuk mempermudah auditor keamanan dalam melakukan pengujian penetrasi jaringan.

---

## 🛠️ Fitur Utama
- **Wireless Attack**: Monitor mode toggle, Handshake capture, WPA/WPA2 Cracking.
- **WPS Auditing**: Reaver & PixieWPS integration.
- **Network Scanning**: Nmap discovery & OS Fingerprinting.
- **Exploitation**: Metasploit integration & Hydra Brute Force.
- **Web Security**: Nikto Scan, SQLMap, & Gobuster.
- **Phishing**: Wifiphisher automated setup.

---

## 💻 Kompatibilitas
Tool ini dirancang untuk berjalan di:
- **Linux** (Kali Linux, Parrot OS, Ubuntu, Xubuntu)
- **Termux** (Dengan akses root untuk fungsi wireless)
- **CMD/PowerShell** (Hanya fungsi tertentu yang tidak membutuhkan driver khusus Linux)

---

## 🚀 Panduan Instalasi

### 1. Di Linux / Xubuntu
Buka terminal dan jalankan:
```bash
git clone [https://github.com/USERNAME-KAMU/wifi-spye.git](https://github.com/USERNAME-KAMU/wifi-spye.git)
cd wifi-spye
pip install colorama
sudo python3 wifi_spye.py
