## Daire çevresi ve alanı hesaplama
print("**** Daire çevresi ve alanını hesaplama ****\n")

## kenar girişleri aşağıda
yariCapi = int(input("Dairenin yarıçapı(cm)? "))

## cevre hesaplama
cevreDaire = 2 * 3.14 * yariCapi
## alan hesaplama
alanDaire = 3.14 * yariCapi * yariCapi

print(f"\nDairenin çevresi {cevreDaire}cm\nÜçgenin alanı {alanDaire} cm2")

input()
