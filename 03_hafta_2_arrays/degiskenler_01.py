ad = "Oğuzhan" # global değişken

def deneme():
    global ad #global olarak tanımlıyor
    ad = "Mehmet"
    print(ad)


deneme()
print(ad)