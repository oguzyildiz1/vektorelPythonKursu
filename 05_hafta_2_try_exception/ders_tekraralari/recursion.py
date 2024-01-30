#bir tam sayıyı bir azalatarak toplam sonucunu bulma

toplam = 0

def toplam_bulma(sayi):
    global toplam

    if sayi == 0:
        return toplam
    else:   # sayi bir değilse
        toplam += sayi
        return toplam_bulma(sayi-1)


sayi = int(input("Bir tam sayı giriniz: "))
print(toplam_bulma(sayi))
