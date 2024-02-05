import mysql.connector

try:
    xxx = mysql.connector.connect(
        host="localhost", # Server.
        user="root", # Kullanıcı adı.
        password="123456" # Şifre
    )

    print("Bağlanılan veritabanı:", xxx)

    secilen_vt = xxx.cursor()
    secilen_vt.execute("USE deneme1;")
    secilen_vt.execute('INSERT INTO ogrenciler (Id, OgrenciNo, AdSoyad, Telefon) VALUES (3, 1021, "Hakan Taşeron", 5535698745)')

    xxx.commit()

    print("Vt successfully updated")

except mysql.connector.Error as xx:
    print("Hata oluştu")
    print(f"Hata kodu: {xx}")


finally:
    xxx.close()