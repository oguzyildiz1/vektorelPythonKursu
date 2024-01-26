import os
import time


## telefon rehberi
def kullaniciEkle(): ## secim icin ayri fonksiyon kullandım
    adi = input("Kayıt edilecek ad, soyad: ")
    numara = input("Kayıt edilecek telefon numarası: ")
    girdi = {"adi" : adi, "num" : numara}
    girdi_str = str(girdi)
    f = open("telefon_rehberi.txt","a")
    f.write(girdi_str)
    time.sleep(1)
    print("\nKişi başarıyla eklendi\n")
    time.sleep(1)
    f.close()
    

def listele():
    try:
        f = open("telefon_rehberi.txt","r")
        okunan = f.read()
        print(okunan)
        f.close()   
    except:
        print("Bir hata oluştu")


def trmenu():
    print("╔" + "═" * 25 + "╗")
    print("║      Telefon Rehberi    ║")
    print("║       1. Kişi ekle      ║")
    print("║       2. Listele        ║")
    print("║       3. Çıkar          ║")
    print("║       4. Çıkış          ║")
    print("╠" + "═" * 25 + "╣")
    print("║Seçiminiz: \t\t  ║")
    print("╚" + "═" * 25 + "╝")

    secim = input()
    if secim == "1":
        kullaniciEkle()
        trmenu()
    elif secim == "2":
        listele()
        trmenu()


#rehbere kaydet


trmenu()

"""
f = open("telrehber.txt","a")
adi = input("Adı, soyadı: ")
numara = input("Telefon numarası: ")
text = {"adi" : adi, "num" : numara}
text_str = str(text)
f.write(text_str)
#f.write(text)

f.close()

print(text)
print(text_str)
"""

#rehber yazdır.