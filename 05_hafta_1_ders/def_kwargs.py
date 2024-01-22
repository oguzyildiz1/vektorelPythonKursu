#**arg : kwargs(dictionary veriyor // **sayi)
def birlestir(**arg1):
    print("Gelen değer :", arg1)

    return arg1["adi"] + " " + arg1["soyadi"]


a = birlestir(adi = "Mustafa", soyadi="Ergen")

print("a: ", a)

for x, y in a:
    print(x,y)