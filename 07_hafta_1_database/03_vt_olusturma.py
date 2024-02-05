import mysql.connector

try:
    xxx = mysql.connector.connect(
        host="localhost", # Server.
        user="root", # Kullanıcı adı.
        password="123456" # Şifre
    )

    print("Bağlanılan veritabanı:", xxx)

    secilen_vt = xxx.cursor()
    secilen_vt.execute("CREATE DATABASE pythondersleri")
    print("VT oluştu.")

except mysql.connector.Error as xx:
    print("Hata oluştu")
    print(f"Hata kodu: {xx}")

