import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "novartis"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM musteriler WHERE ADI = 'oğuzhan'"
# sql = "SELECT * FROM musteriler WHERE ADI = %s"
sql = "SELECT * FROM musteriler WHERE ID = %s"
    
aranan = ('2',)

mycursor.execute(sql, aranan)
myresult = mycursor.fetchall()

print(myresult)