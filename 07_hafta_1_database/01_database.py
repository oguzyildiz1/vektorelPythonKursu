import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234"
    )

    print("başarıyla bağlandı")
except:
    pass