#python exception parameters diye geçiyor.

while True:
    try:
        sayi1 = int(input("Bir sayı giriniz:"))
        sayi2 = int(input("Bir sayı giriniz:"))
        print("Toplam: ", sayi1 + sayi2)
        break
    except:
        print("Bir hata oluştu")
input()