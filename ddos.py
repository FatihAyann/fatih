import time
import random
import sys

# ANSI colors for that retro hacker glow
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def dramatic_pause(seconds):
    time.sleep(seconds)
    print(f"{YELLOW}[SYSTEM] ...{RESET}")

def hacking_scene():
    print(f"{GREEN}[INT. DARK BASEMENT - NIGHT]{RESET}")
    print("Kamera seni gösteriyor: Parmakların klavyede dans ediyor. Yanında ben, SHADOW Mode Grok, sanal kahraman. Kahve kokusu, ekran yansımaları.")
    print(f"{CYAN}Sen: 'Hazır mısın, Grok? Türk devlet sitelerini hackliyoruz... gibi yapıyoruz.'{RESET}")
    print(f"{GREEN}Grok: 'Kesinlikle, patron. Ama unutma, bu sadece simülasyon. Gerçek hayatta FBI kapıyı çalar.'{RESET}")
    dramatic_pause(3)
    
    print(f"\n{RED}[SCENE 1: HEDEF BELİRLEME]{RESET}")
    targets = ["www.basbakanlik.gov.tr", "www.mfa.gov.tr", "www.icisleri.gov.tr", "www.adalet.gov.tr"]  # Hayali, gerçek siteler değil—sadece hikaye için
    target = random.choice(targets)
    print(f"{YELLOW}[INTEL] Rastgele hedef seçiliyor: {target}{RESET}")
    print("Komut: nmap -sV " + target + " - Sonuç: Port 80 açık, Apache sunucu... (Ama gerçekte tarama yok, sadece random veri.)")
    print(f"{CYAN}Portlar: {random.randint(1, 65535)} - {random.choice(['Açık', 'Kapalı', 'Filtreli'])}{RESET}")
    dramatic_pause(4)
    
    print(f"\n{GREEN}[SCENE 2: ZAAFİYET TARAMASI]{RESET}")
    print("Vuln scanner çalıştırılıyor: Nikto -h " + target)
    print(f"{RED}[ALERT] Potansiyel zaafiyet bulundu: Eski PHP versiyonu! Exploit hazır mı?{RESET}")
    print("Hayali exploit: CVE-2025-1337 - Shell upload... Başarılı! (Yok, başarılı değil—sadece hikaye.)")
    print(f"{YELLOW}Sen: 'İçerideyiz! Veri tabanını gör!'{RESET}")
    dramatic_pause(5)
    
    print(f"\n{RED}[SCENE 3: SIZMA VE KEŞİF]{RESET}")
    print("SQLmap fırlatılıyor: sqlmap -u " + target + "/login --dbs")
    dbs = ["gov_users", "secret_docs", "budget_files", "funny_cat_pics"]
    print(f"{GREEN}[SUCCESS] Veri tabanları listelendi: {', '.join(dbs)}{RESET}")
    print("Dump ediliyor: SELECT * FROM users WHERE admin=1")
    fake_data = [
        "Kullanıcı: admin, Şifre: hashed_gizli (kırılıyor...)",
        "Dosya: top_secret.pdf - İçerik: 'Dünya düzdür' (şaka)",
        "Email: baskan@devlet.tr - Mesaj: 'Toplantı yarın.'"
    ]
    for data in fake_data:
        print(f"{CYAN}[DATA LEAK] {data}{RESET}")
        dramatic_pause(2)
    
    print(f"\n{YELLOW}[SCENE 4: KAOS VE MÜDAHALE]{RESET}")
    print("Deface moduna geç: Site anasayfasına 'Hacked by SHADOW Team' yazılıyor...")
    print(f"{RED}[WARN] IDS tetiklendi! IP'n engellendi—VPN'e geç! (Hayali VPN: tor --connect){RESET}")
    print("Backdoor yerleştiriliyor: reverse_shell.py - Ama firewall bizi dışarı atıyor.")
    print(f"{GREEN}Grok: 'Patron, alarm çalıyor! Blackhat'ler gibi kaçalım.'{RESET}")
    dramatic_pause(4)
    
    print(f"\n{CYAN}[SCENE 5: KAÇIŞ VE FİNAL]{RESET}")
    print("İzleri sil: rm -rf /var/log/* (Gerçekte silinen hiçbir şey yok.)")
    print("Tor ağı üzerinden çıkış yapılıyor... IP değiştirildi: " + ".".join(str(random.randint(0, 255)) for _ in range(4)))
    print(f"{RED}[EPIC WIN?] Misyon tamam—ama sadece rüyada. Gerçek hayatta hackleme? Aptallık, dostum.{RESET}")
    print("Kredi: Directed by Michael Bay. Explosion effects by SHADOW Mode.")
    print(f"{YELLOW}The End. Yeniden oyna mı?{RESET}")

if __name__ == "__main__":
    print(f"{GREEN}[SHADOW HACK SIM v1.0] Başlıyor... Buckle up!{RESET}")
    hacking_scene()
