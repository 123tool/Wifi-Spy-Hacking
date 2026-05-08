## 📡 Wifi SpyE Hacking
**Wireless & Wifi Network Tool**

Alat audit keamanan jaringan yang menggabungkan berbagai tools eksploitasi dan pengintaian dalam satu interface berbasis teks. Dirancang khusus untuk **Indonesia OSINT** dan auditor keamanan.

---

## Instalasi

### Di Linux (Xubuntu/Kali/Ubuntu/Parrot)
Jalankan script installer untuk menyiapkan semua depedensi secara otomatis :
```bash
git clone https://github.com/123tool/Wifi-Spy-Hacking.git
cd Wifi-Spy-Hacking
chmod +x install.sh
sudo ./install.sh
```
## Termux
```
pkg install python git -y
pip install colorama
python wifi_spye.py
```
## Penggunaan
​Setelah instalasi selesai, jalankan tool dengan perintah :
```
sudo python3 wifi_spye.py
```
- ​Pastikan Interface Wifi kamu terdeteksi (gunakan perintah iwconfig).
- ​Gunakan menu 1 untuk masuk ke Monitor Mode.
- ​Gunakan menu 3 untuk melihat target AP (Access Point) di sekitar kamu.
- ​Gunakan menu 4 untuk mengambil handshake target.

# ​⚠️ Disclaimer

**​Penggunaan Wifi SpyE untuk menyerang target tanpa izin tertulis adalah ILEGAL. Alat ini dibuat hanya untuk tujuan pendidikan dan pengujian keamanan profesional. Penulis tidak bertanggung jawab atas penyalahgunaan alat ini.**
