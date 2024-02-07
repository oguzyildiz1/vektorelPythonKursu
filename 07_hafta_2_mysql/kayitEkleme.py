import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="123456",database="deneme1")

mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN NufusNo INT(10)")
#mycursor.execute("ALTER TABLE ogrenciler ADD COLUMN Sınıf VARCHAR(5)")

ad = input("İsim soyisim? ")
no = input("Numara? ")

a = "INSERT INTO ogrenciler (AdSoyad, Telefon) VALUES %s %s"
b = (ad, no)

mycursor.execute(a, b)

mydb.commit()

print(mycursor.rowcount, "kayık eklendi.")