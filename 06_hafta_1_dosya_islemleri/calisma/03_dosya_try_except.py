try:
    dosya = open("rehber.txt","r")
    print(" Rehber kayıt listesi ")
    print("═══════════════════════")
    a= 1
    for kayit in dosya.readlines():
        print(a, kayit)
        a+=1
except:
    print("Dosya bulunamadı")
    input()
