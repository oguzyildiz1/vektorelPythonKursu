## Üçgen çevresi ve alanı hesaplama
print("**** Üçgen çevresi ve alanını hesaplama ****\n")

## kenar girişleri aşağıda
kenarTaban = int(input("Taban kenar(cm)? "))
kenarIki= int(input("2. kenar(cm)? "))
kenarUc = int(input("3. kenar(cm)? "))
yukseklik = int(input("Yükseklik(cm)?"))

## cevre hesaplama
cevreUcgen = kenarTaban + kenarIki + kenarUc
## alan hesaplama
alanUcgen = (kenarTaban * yukseklik) / 2

print(f"Üçgenin çevresi {cevreUcgen}cm\nÜçgenin alanı {alanUcgen} cm2")

input()
