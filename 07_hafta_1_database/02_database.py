import mysql.connector

try:
    xxx = mysql.connector.connect(
        host="localhost", # Server.
        user="root", # Kullanıcı adı.
        password="123456" # Şifre
    )

    print("Bağlanılan veritabanı:", xxx)

except:
    print("Hata oluştu")
