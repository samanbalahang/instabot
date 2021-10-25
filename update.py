from mysql import connector

mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_instabot"
)
mycursor = mydb.cursor()

sql = "UPDATE urls SET belongs_to = %s WHERE id = %s"
val = ('https://www.instagram.com/bari.editor/', 2)
mycursor.execute(sql, val)
# mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
# print(mydb)
