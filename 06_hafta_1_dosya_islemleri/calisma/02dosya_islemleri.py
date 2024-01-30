#türkçe karakter kullanımı 

abc = open("program1.py","w",encoding="utf-8") #utf-8 girmek gerekiyor.

abc.write("#bu program python tarafından otomatik olarak oluşturulmuştur.")
abc.write("\na=input('Bir kelime gir: ')")
abc.write("\nprint(a * 20)")
abc.write("\ninput()")
abc.close()