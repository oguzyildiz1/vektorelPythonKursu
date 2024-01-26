import os
import time

os.mkdir("veriler3")

dosya = open("./veriler/rehber.txt","w")
dosya.write("Deneme1")
dosya.close()

time.sleep(6)
os.remove("rehber1.txt")