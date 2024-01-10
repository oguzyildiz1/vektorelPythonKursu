import datetime
#strftime() kullanımı (date ile gelen tarihi formatlıyor)

print("Bugün", datetime.date.today())
print("Şimdi", datetime.datetime.now())
simdi = datetime.datetime.now()

print(simdi.strftime("%m %D %Y")) #time'ı formatlıyor. (Bakılabiliyor.)
print()
