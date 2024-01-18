meyveler = ["elma","armut","karpuz"]

meyveler.append("kiraz")

meyveler.insert(3,"Muz")
print(meyveler)

sebzeler = ["Kereviz","Lahana",
"Prasa"]

alinacaklar = meyveler + sebzeler
print(alinacaklar)

alinacaklar.pop(3)
print(alinacaklar)
alinacaklar.pop(5)
print(alinacaklar)
alinacaklar.sort()

print(alinacaklar)
alinacaklar.reverse()
print(alinacaklar)
alinacaklar.append("kiraz")
print(alinacaklar)
print(alinacaklar.count("kiraz")) 