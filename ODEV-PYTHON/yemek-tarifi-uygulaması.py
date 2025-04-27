class Tarif:
    def __init__(self, ad, malzemeler, tarif_icerigi):
        self.ad = ad
        self.malzemeler = malzemeler
        self.tarif_icerigi = tarif_icerigi
        self.degerlendirmeler = []

    def tarif_ekle(self):
        print(f"{self.ad} tarifi eklendi.")

    def tarif_ara(self, arama_kelimesi):
        if arama_kelimesi.lower() in self.ad.lower():
            print(f"Tarif bulundu: {self.ad}")
        else:
            print("Tarif bulunamadı.")

    def tarif_degerlendir(self, degerlendirme):
        self.degerlendirmeler.append(degerlendirme)
        print(f"Tarif {self.ad} için {degerlendirme} puanı verildi.")
    
    def ortalama_degerlendirme(self):
        if self.degerlendirmeler:
            return sum(self.degerlendirmeler) / len(self.degerlendirmeler)
        return 0

    def tarif_goruntule(self):
        print(f"\n{self.ad} Tarifi")
        print("Malzemeler:")
        for malzeme in self.malzemeler:
            print(f"- {malzeme}")
        print(f"Tarif İçeriği: {self.tarif_icerigi}")
        print(f"Ortalama Değerlendirme: {self.ortalama_degerlendirme():.2f}")


class Malzeme:
    def __init__(self, ad, miktar):
        self.ad = ad
        self.miktar = miktar

    def __str__(self):
        return f"{self.miktar} {self.ad}"

class Kullanici:
    def __init__(self, ad, sifre):
        self.ad = ad
        self.sifre = sifre
        self.tarifler = []

    def tarif_ekle(self, tarif):
        self.tarifler.append(tarif)
        tarif.tarif_ekle()

    def tarif_degerlendir(self, tarif, degerlendirme):
        tarif.tarif_degerlendir(degerlendirme)

def tarif_olustur():
    print("Yeni tarif oluşturmak için gerekli bilgileri girin.")
    
    ad = input("Tarif adı: ")

    malzemeler = []
    while True:
        malzeme_ad = input("Malzeme adı (tamamlamak için 'a' tuşuna basın): ")
        if malzeme_ad.lower() == 'a':
            break
        malzeme_miktar = input(f"{malzeme_ad} için miktar: ")
        malzeme = Malzeme(malzeme_ad, malzeme_miktar)
        malzemeler.append(malzeme)

    tarif_icerigi = input("Tarif içeriği: ")

    tarif = Tarif(ad, malzemeler, tarif_icerigi)
    return tarif

def kullanici_olustur():
    ad = input("Kullanıcı adı: ")
    sifre = input("Kullanıcı şifresi: ")
    kullanici = Kullanici(ad, sifre)
    return kullanici

def ana_menu():
    print("\n    -Yemek Tarifi Uygulaması")
    print("1. Kullanıcı oluştur.")
    print("2. Tarif oluştur.")
    print("3. Mevcut tariflerden birini seç ve değerlendir.")
    print("4. Mevcut tariflerden birini seç ve görüntüle.")
    print("5. Çıkış.")

def mevcut_tarifleri_goster(tarifler):
    print("\n   Mevcut Tarifler   ")
    if not tarifler:
        print("Henüz tarif eklenmedi.")
    else:
        for idx, tarif in enumerate(tarifler, start=1):
            print(f"{idx}. {tarif.ad}")

kullanici = None
tarifler = []

while True:
    ana_menu()
    secim = input("Seçiminizi yapın (1-5): ")

    if secim == "1":
        kullanici = kullanici_olustur()
        print(f"{kullanici.ad} kullanıcısı oluşturuldu.")
    elif secim == "2":
        if kullanici:
            tarif = tarif_olustur()
            tarifler.append(tarif)
            kullanici.tarif_ekle(tarif)
        else:
            print("Lütfen önce bir kullanıcı oluşturun.")
    elif secim == "3":
        if tarifler:
            mevcut_tarifleri_goster(tarifler)
            try:
                secilen_tarif_index = int(input("\nDeğerlendirmek istediğiniz tarifin numarasını girin: ")) - 1
                if 0 <= secilen_tarif_index < len(tarifler):
                    secilen_tarif = tarifler[secilen_tarif_index]
                    degerlendirme = int(input(f"Tarife {secilen_tarif.ad} puan (1-5): "))
                    kullanici.tarif_degerlendir(secilen_tarif, degerlendirme)
                    print(f"Ortalama Değerlendirme: {secilen_tarif.ortalama_degerlendirme():.2f}")
                else:
                    print("Geçersiz numara.")
            except ValueError:
                print("Lütfen geçerli bir numara girin.")
        else:
            print("Henüz tarif oluşturulmamış.")
    elif secim == "4":
        if tarifler:
            mevcut_tarifleri_goster(tarifler)
            try:
                secilen_tarif_index = int(input("\nGörüntülemek istediğiniz tarifin numarasını girin: ")) - 1
                if 0 <= secilen_tarif_index < len(tarifler):
                    secilen_tarif = tarifler[secilen_tarif_index]
                    secilen_tarif.tarif_goruntule()
                else:
                    print("Geçersiz numara.")
            except ValueError:
                print("Lütfen geçerli bir numara girin.")
        else:
            print("Henüz tarif oluşturulmamış.")
    elif secim == "5":
        print("Çıkılıyor...Görüşürüz.")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")