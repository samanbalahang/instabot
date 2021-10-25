from mysql import connector
from pySqlconn import connecting
from loginInsta import cInstaLogins
from gatherIds import cGatherId
import time
mydb = connecting.conn()
mycursor = mydb.cursor()


class cSeachTerms:
    def __init__(self,searchTerms:list,userName,password):
        print(searchTerms)
        print(userName)
        print(password)
        for item in searchTerms:
            search = item["serch"]
            desc = item["desc"]
            sql = "INSERT INTO search_terms (serch_title,search_desc) VALUES (%s, %s)"
            val = (search,desc )
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            browser = cInstaLogins.LogIn(self,userName,password)
            search = item["serch"]
            cGatherId.gatherId(self,browser,search)
            time.sleep(10)
            


# searchTerms = [
#     {"serch": "#احمد_کلاته" , "desc": "رشد پیچ"},
#     {"serch": "#رشد_پیج" , "desc": "رشد پیج"},
#     {"serch": "#تولید_محتوا" , "desc": "رشد پیج"},
# ]
# i=0
# for item in searchTerms:
#     search = item["serch"]
#     desc = item["desc"]
#     sql = "INSERT INTO search_terms (serch_title,search_desc) VALUES (%s, %s)"
#     val = (search,desc )
#     mycursor.execute(sql, val)
#     mydb.commit()
#     print(mycursor.rowcount, "record inserted.")
#     print(mydb)




# p1 = InstaBot("cobco_perfume_ca", "perfumec0rp0ratio")
# for item in searchTerms:
#     # print(item["serch"])
#     # i+=1
#     search = item["serch"]
#     p1.gatherIds(search)
#     time.sleep(10)
