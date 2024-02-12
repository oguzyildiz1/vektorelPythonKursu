#like ile ...
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="deneme1")

mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN NufusNo INT(10)")
#mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN Sınıf VARCHAR(5)")


sql = "SELECT * FROM ogrenciler;"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    for a in x:
        print(a, end=" ")
    print()

sql = "UPDATE ogrenciler SET Telefon='5556669988' WHERE AdSoyad='Oğuzhan Yıldız'"
mycursor.execute(sql)
mydb.commit() #commit yapılması gerekiyor.

myresult = mycursor.fetchall()

for x in myresult:
    for a in x:
        print(a, end=" ")
    print()