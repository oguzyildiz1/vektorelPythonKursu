# args(tuple veriyor *sayi) 
# yollanacak parametre sayısı belli değilse args kullanılıyor.

def toplama(*sayi):#dizi değer olarak alıyor args
    toplam = 0
    print(sayi[0])

    for x in sayi:
        toplam += x

    return toplam


print("toplam : ", toplama(10,20,23))
print("-----------------------------")


def ortalama(*sayi): 
    toplam = 0

    for x in sayi:
        toplam += x
    
    ortalama = toplam / len(sayi)
    print(ortalama)


ortalama(12,21,12,23)