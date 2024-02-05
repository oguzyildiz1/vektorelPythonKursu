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


secilen_vt = xxx.cursor() #veri tabanı seçim işlemi USE .....
secilen_vt.execute("SHOW DATABASES")
print("\nVeri tabanları\n")

for x in secilen_vt: print(x)

secilen_vt.execute("USE okulvt")
secilen_vt.execute("")