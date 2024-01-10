from datetime import date
#yaş hesaplam
today1 = date.today()

print("yıl",today1.year)
print("ay",today1.month)
print("gün",today1.day)

yil = int(input("Doğum yılın nedir?"))
print("Sen: ",today1.year-yil)





