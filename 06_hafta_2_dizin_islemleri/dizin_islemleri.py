import os

liste1 = os.listdir()
pySayisi = 0

for a in liste1:
    if a.endswith(".py"): pySayisi += 1
    if os.path.isfile(a): print(a, "\t\t\t","dosya")
    if os.path.isdir(a): print(a,"\t\t\t", "<DIR>")


print("Dosya sayısı: ", pySayisi)

print(os.getcwd())

