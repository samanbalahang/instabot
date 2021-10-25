from connection import connecting
mydb = connecting.conn

mycursor = mydb.cursor()


sql = "INSERT INTO urls (url,description) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
