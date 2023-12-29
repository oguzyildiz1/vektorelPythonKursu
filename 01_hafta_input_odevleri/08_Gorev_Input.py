## İdeal kilo hesaplama programı
print("**** İdeal kilo hesaplama programı ****\n")

## boy girişleri aşağıda
boy = int(input("Boyunuz(cm)? "))
## ideal kilo heaplama
idealKad = 45.5 + (2.3 / 2.54) *(boy - 152.4)
idealErk = 50 + (2.3 / 2.54) * (boy - 152.4)

print(f"Ideal kilonuz kadın iseniz {idealKad}\nErkek iseniz {idealErk}.")

input()
