from pageOfPost import PageOfpost
from text import InstaBot
from pageOfPost import PageOfpost
from instaLogin import instaLogins
from mysql import connector
import time
mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_instabot"
)
mycursor = mydb.cursor()

# sql = "INSERT INTO search_terms (serch_title,search_desc) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
# print(mydb)



searchTerms = [
    {"serch": "#احمد_کلاته" , "desc": "رشد پیچ"},
    {"serch": "#رشد_پیج" , "desc": "رشد پیج"},
    {"serch": "#تولید_محتوا" , "desc": "رشد پیج"},
]
# i=0
for item in searchTerms:
    # print(item["serch"])
    # i+=1
    search = item["serch"]
    desc = item["desc"]
    sql = "INSERT INTO search_terms (serch_title,search_desc) VALUES (%s, %s)"
    val = (search,desc )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    print(mydb)




p1 = InstaBot("cobco_perfume_ca", "perfumec0rp0ratio")
for item in searchTerms:
    # print(item["serch"])
    # i+=1
    search = item["serch"]
    p1.gatherIds(search)
    time.sleep(10)
