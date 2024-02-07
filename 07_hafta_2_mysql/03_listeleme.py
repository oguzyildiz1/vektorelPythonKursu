#isim ile verileri yazdırma
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="deneme1")

mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN NufusNo INT(10)")
#mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN Sınıf VARCHAR(5)")

mycursor.execute("SELECT * FROM ogrenciler WHERE AdSoyad = 'Oğuzhan Yıldız'")
xxx = mycursor.fetchall()

for x in xxx:
    print(x)