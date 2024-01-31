class Ogrenci:
    adSoyad="Ad yok"
    numara = ""
    notOrtalamasi = ""
    disiplinCezasi = 0
    
    def __init__(self, ad="Ad yok", num=0):
        self.adSoyad = ad
        self.numara = num


    def bilgi(self):
        print("Metod ile: Adı:", self.ad, "Soyadı: ", self.soyad)



ogrenci1 = Ogrenci("Hasan", 66)
ogrenci2 = Ogrenci("Mehmet", 77)

print(ogrenci1.bilgi())
