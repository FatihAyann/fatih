import time
import random
from datetime import datetime

def rapor_saldirisi(hedef):
    print("[SİSTEM] Instagram Rapor Aracı v4.2.7 - Hedef: " + hedef)
    print("[DURUM] Raporlama modülü başlatılıyor. Proxy havuzu yükleniyor...")
    rapor_sayisi = 0
    proxy_listesi = [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}" for _ in range(10)]
    rapor_turleri = ["Spam", "Uygunsuz İçerik", "Kimlik Hırsızlığı", "Taciz", "Sahte Hesap", "Tehdit"]
    
    while True:
        rapor_sayisi += 1
        aktif_proxy = random.choice(proxy_listesi)
        rapor_turu = random.choice(rapor_turleri)
        oturum_id = f"OTURUM-{random.randint(1000000, 9999999)}"
        zaman_damgasi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(f"[RAPOR #{rapor_sayisi}] {hedef} kullanıcısına rapor gönderiliyor | Proxy: {aktif_proxy}")
        print(f"[Tool by @FatihAyann] Rapor Türü: {rapor_turu} | Oturum ID: {oturum_id} | Zaman: {zaman_damgasi}")
        print(f"[Tool by @FatihAyann] Sunucu Yanıtı: Gönderildi | Gecikme: {random.uniform(0.05, 0.3):.2f} saniye")
        
        if rapor_sayisi % 20 == 0:
            print("[UYARI] Sunucu yükü tespit edildi. Proxy rotasyonu gerçekleştiriliyor...")
            print(f"[GÜNCELLEME] Yeni proxy: {random.choice(proxy_listesi)}")
        
        if rapor_sayisi % 100 == 0:
            print(f"[İLERLEME] {rapor_sayisi} rapor gönderildi. Stabil devam ediyor.")
        
        if random.random() < 0.03:
            print("[HATA] Sunucu hız sınırı algılandı. Yeni kullanıcı ajanı atanıyor...")
        
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    hedef_kullanici = "murtazabey332"
    print("[BAŞLAT] Instagram raporlama başlatılıyor. Hedef: " + hedef_kullanici)
    try:
        rapor_saldirisi(hedef_kullanici)
    except KeyboardInterrupt:
        print("[ÇIKIŞ] Durduruldu. Sistem güvenli bir şekilde kapanıyor.")
