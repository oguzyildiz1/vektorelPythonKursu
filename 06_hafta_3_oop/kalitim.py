class Ilan():
    def  __init__(self, n, b, s, a):
        self.ilanNo = n
        self.ilanBaslik = b
        self.ilanSahibi = s
        self.ilanAciklama = a
        
    def bilgi(self):
        print("No:", self.ilanNo, "Başlık:", self.ilanBaslik)

    def bilgi1(self):
        return "No: " + self.ilanNo + "Başlık: ", self.ilanBaslik


    def kaydet(self):
        d= open("kayit.txt","w")
        kb = f"{self.ilanNo} {self.ilanBaslik} {self.ilanSahibi}\n"
        d.write(kb)
        d.close()
        self.bilgi()


class Ev(Ilan):
    def __init__(self, n, b, s, a , o= "--"):
        self.odaSayisi = o
    def bilgi(self):
        print("Oda sayısı: ", self.odaSayisi, "Açıklaması: ", )

# --------------- encapsulation ---------------------------------------
class Arac(Ilan):
    aracMarkasi = ""
    def __init__(self, n, b, s, a, m, f):
        self.aracMarkasi = a
        self.__fiyat = f # __ ile encapsulation yapılıyor.

    def bilgi(self):
        print("Marka: ", self.aracMarkasi, "Fiyatı: ", self.__fiyat)

    def fiyatAyarla(self, abc):
        self.__fiyat = abc 

# -------------- kalitim ------------------------

class KiralikEv(Ev):
    def __init__(self, n, b, s, a, o, kf):
        super().__init__(n, b, s, a, o) # kalitim kodu
        
        self.odaSayisi = 5
        self.kiraFiyati = kf

    def bilgi(self):
        print("Kiralik ev", "Fiyati: ", self.kiraFiyati)


ilan1 = Ilan(123, "Ev", "Ahmet Kara", "Evi hemen satmam gerektiği için bu işi halletttim.")

ilan2 = Ev(143, "Ev", "Tarık Sorar", "Kiralık ev hemen teslim.", 3)
ilan3 = Arac(1233, "Araba","Mustafa Korkmaz","Açıklama","Volvo", 123123)

ilan4 = KiralikEv(145, "Kiralik Ev", "Oguz Sorar", "Kiralık ev hemen teslim.", 3, 1000)

ilan1.bilgi()

ilan2.bilgi()
ilan3.bilgi()
ilan2.odaSayisi = 5
ilan3.aracMarkasi = "Toyota"
ilan3.__fiyat = 565555
ilan3.fiyatAyarla(569999)

ilan3.bilgi()

ilan4.bilgi()
