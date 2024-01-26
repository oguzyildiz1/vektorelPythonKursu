
#"x" #create(oluştur)

# "a" append(ekle)

# "w" write
import os
import time


yazilacak = ""

ad = input("Kaydedilecek ad ve soyadı:")
numara = input("Kaydedilecek numara  :")


dosya = open("rehber111.txt","a")
dosya.write("Royem 53223232323\n")

dosya.write("Oguzh 53123234223\n")

dosya.close()