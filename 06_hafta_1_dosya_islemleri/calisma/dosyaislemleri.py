import os


def dosya_islemleri():
    abc = open("rehber.txt","w")
    abc.write("Buraya kaydedilen veri.\nİkinci satıra geçtik.\n")
    abc.write("İkinci satır ise\n\n")
    abc.close()


dosya_islemleri()