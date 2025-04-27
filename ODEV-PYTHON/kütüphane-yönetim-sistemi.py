class Kitap:
    def __init__(self, kitap_id, ad, yazar):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.durum = "Mevcut"

    def bilgileri_goster(self):
        return f"Kitap ID: {self.kitap_id}, Ad: {self.ad}, Yazar: {self.yazar}, Durum: {self.durum}"
    
    def durumu_guncelle(self, yeni_durum):
        self.durum = yeni_durum

class Uye:
    def __init__(self, uye_id, ad, soyad):
        self.uye_id = uye_id
        self.ad = ad
        self.soyad = soyad
        self.odunc_kitaplar = []
    
    def bilgileri_goster(self):
        return f"Üye ID: {self.uye_id}, Ad: {self.ad} {self.soyad}, Ödünç Kitaplar: {[kitap.ad for kitap in self.odunc_kitaplar]}"

    def odunc_al(self, kitap):
        if kitap.durum == "Mevcut":
            kitap.durumu_guncelle("Ödünç Alındı")
            self.odunc_kitaplar.append(kitap)
            print(f"{kitap.ad} kitabı ödünç alındı.")
        else:
            print(f"{kitap.ad} kitabı şu anda mevcut değil.")

    def iade_et(self, kitap):
        if kitap in self.odunc_kitaplar:
            kitap.durumu_guncelle("Mevcut")
            self.odunc_kitaplar.remove(kitap)
            print(f"{kitap.ad} kitabı iade edildi.")
        else:
            print(f"{kitap.ad} kitabı ödünç alınmamış.")

class Odunc:
    def __init__(self, uye, kitap):
        self.uye = uye
        self.kitap = kitap

    def odunc_bilgisi(self):
        return f"{self.uye.ad} {self.uye.soyad} -> {self.kitap.ad}"

class OduncSistemi:
    def __init__(self):
        self.kitaplar = []
        self.uyeler = []
        self.oduncler = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)

    def uye_ekle(self, uye):
        self.uyeler.append(uye)

    def kitaplari_listele(self):
        for kitap in self.kitaplar:
            print(kitap.bilgileri_goster())

    def uyeleri_listele(self):
        for uye in self.uyeler:
            print(uye.bilgileri_goster())

    def oduncleri_listele(self):
        for odunc in self.oduncler:
            print(odunc.odunc_bilgisi())

    def islem_yap(self):
        while True:
            print("\n   -KÜTÜPHANE MENÜSÜ     ")
            print("1) Kitapları Listele.")
            print("2) Üyeleri Listele.")
            print("3) Kitap Ödünç Al.")
            print("4) Kitap İade Et.")
            print("5) Yeni Kitap Ekle.")
            print("6) Yeni Üye Ekle.")
            print("7) Ödünç Alınan Kitapları Listele.")
            print("8) Çıkış.")
            
            try:
                secim = int(input("Ne yapmak istiyorsun? (Seçim yap: 1-8): "))
            except ValueError:
                print("Lütfen sadece rakam gir. ")
                continue

            if secim == 1:
                self.kitaplari_listele()

            elif secim == 2:
                self.uyeleri_listele()

            elif secim == 3:
                uye_id = int(input("Ödünç alacak üyenin ID'sini gir: "))
                kitap_id = int(input("Ödünç alınacak kitabın ID'sini gir: "))
                uye = self.uye_bul(uye_id)
                kitap = self.kitap_bul(kitap_id)
                if uye and kitap:
                    uye.odunc_al(kitap)
                    self.oduncler.append(Odunc(uye, kitap))
                else:
                    print("Üye veya kitap bulunamadı.")

            elif secim == 4:
                uye_id = int(input("İade yapacak üyenin ID'sini gir: "))
                kitap_id = int(input("İade edilecek kitabın ID'sini gir: "))
                uye = self.uye_bul(uye_id)
                kitap = self.kitap_bul(kitap_id)
                if uye and kitap:
                    uye.iade_et(kitap)
                    
                    self.oduncler = [odunc for odunc in self.oduncler if not (odunc.uye == uye and odunc.kitap == kitap)]
                else:
                    print("Üye veya kitap bulunamadı.")

            elif secim == 5:
                kitap_id = int(input("Yeni kitabın ID'sini gir: "))
                ad = input("Kitap adını gir: ")
                yazar = input("Yazar adını gir: ")
                yeni_kitap = Kitap(kitap_id, ad, yazar)
                self.kitap_ekle(yeni_kitap)
                print(f"{ad} kitabı eklendi.")

            elif secim == 6:
                uye_id = int(input("Yeni üyenin ID'sini gir: "))
                ad = input("Üyenin adını gir: ")
                soyad = input("Üyenin soyadını gir: ")
                yeni_uye = Uye(uye_id, ad, soyad)
                self.uye_ekle(yeni_uye)
                print(f"{ad} {soyad} üyesi eklendi.")

            elif secim == 7:
                self.oduncleri_listele()

            elif secim == 8:
                print("Çıkılıyor... Görüşürüz.")
                break

            else:
                print("Yanlış seçim yaptın, menüde olmayan bir rakam yazdın.")

    def uye_bul(self, uye_id):
        for uye in self.uyeler:
            if uye.uye_id == uye_id:
                return uye
        return None

    def kitap_bul(self, kitap_id):
        for kitap in self.kitaplar:
            if kitap.kitap_id == kitap_id:
                return kitap
        return None

odunc_sistemi = OduncSistemi()

kitap1 = Kitap(1, "Aşk ve Gurur", "Jane Austen")
kitap2 = Kitap(2, "Sefiller", "Victor Hugo")
kitap3 = Kitap(3, "Anna Karenina", "Tolstoy")
kitap4 = Kitap(4, "Suç ve Ceza", "Dostoyevski")
kitap5 = Kitap(5, "Romeo ve Juliet", "Shakespeare")


uye1 = Uye(1, "Beren", "Yüksel")
uye2 = Uye(2, "Nisa", "Kurt")
uye3 = Uye(3, "Çınar", "Şahin")
uye4 = Uye(4, "Nejla", "Yılmaz")
uye5 = Uye(5, "Defne", "Özdağ")

odunc_sistemi.kitap_ekle(kitap1)
odunc_sistemi.kitap_ekle(kitap2)
odunc_sistemi.kitap_ekle(kitap3)
odunc_sistemi.kitap_ekle(kitap4)
odunc_sistemi.kitap_ekle(kitap5)

odunc_sistemi.uye_ekle(uye1)
odunc_sistemi.uye_ekle(uye2)
odunc_sistemi.uye_ekle(uye3)
odunc_sistemi.uye_ekle(uye4)
odunc_sistemi.uye_ekle(uye5)

odunc_sistemi.islem_yap()