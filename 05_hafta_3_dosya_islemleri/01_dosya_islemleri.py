

#"x" #create(oluştur)

# "a" append(ekle)

# "w" write


for a in range(1, 11):
    abc = open(f"rehber{a}.txt","w")

    abc.write("Dosya kadedilen satıra yazılıyor.\n")

    abc.write("İkinci satıra yazılıyor.\n")

    abc.write("!!!")
    abc.close()