#like ile ...
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="deneme1")

mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN NufusNo INT(10)")
#mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN Sınıf VARCHAR(5)")

aranan = input("Aradığınız isim? ")
sql = "SELECT * FROM ogrenciler WHERE AdSoyad = %s"

aranan_x = (f"{aranan}",)

mycursor.execute(sql, aranan_x)
myresult = mycursor.fetchall()

for x in myresult:
    for a in x:
        print(a, end=" ")
    print()