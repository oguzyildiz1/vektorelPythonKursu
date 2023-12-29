## not hesaplama
print("**** Not hesaplama programı ****\n")

## not girişleri aşağıda
yazili1 = int(input("1. yazılı notu? "))
yazili2 = int(input("2. yazılı notu? "))
perfNotu = int(input("Performans notu? "))

## hesaplama
ortalama = yazili1 * 0.4 + yazili2 * 0.4 + perfNotu * 0.2

print("Not ortalamanız: {}".format(ortalama))

input()
