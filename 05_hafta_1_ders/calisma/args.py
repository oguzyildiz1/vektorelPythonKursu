def toplama(*para1):
    print(para1)
    toplam = 0

    for i in para1:
        toplam += i
    
    return toplam
    




print(toplama(10,12,23,22,45))
print(toplama(10,10,10))