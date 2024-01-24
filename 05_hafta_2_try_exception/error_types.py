#python exception parameters diye geçiyor.

while True:
    try:
        sayi1 = int(input("Bir sayı giriniz:"))
        sayi2 = int(input("Bir sayı giriniz:"))
        print("Bölüm: ", sayi1 / sayi2)
        break
    except ValueError:
        print("Girilen değerlerde sorun var.") # daha spesifik açıklama yazmak gerekiyor

    except ZeroDivisionError:
        print("0'a bölüm hatası.")

    except :
        print("Bir hata oluştu.")

    finally: 
        print("Hata oluşma ihtimali olan blok bitti.")

input()