import os

os.chdir("C:/Users/yildi/OneDrive/Desktop/python/vektorelBilisim/github/vektorelPythonKursu/06_hafta_1_dosya_islemleri/calisma")

dosya = open("orhanYildiz.txt","w")

dosya.write("Selamlar Orhan Yıldız")

dosya.close()