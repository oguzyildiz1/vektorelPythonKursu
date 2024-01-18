a = " "
b = "Selamlar Nasılsınız? İyiyim"

if " " not in "Selamlar Nasılsınız?":
    print("Boşluk yok")
else:
    print("Boşluk var")
    print(len(b))
    print("Selamlar ".count(" "))
    print(b.index(" "))
    print(b[0:b.index(" ")])
    print(b[b.index(" ")+1:])

print(b.split())