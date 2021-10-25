from mysql import connector

mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_instabot"
)
excutable = mydb.cursor(dictionary=True)

class getrandComments:
    def randComments():    
        sql = "Select * from comments ORDER BY RAND() LIMIT 1"
        excutable.execute(sql)
        myresult = excutable.fetchall()
        for x in myresult: 
            # return x['comment']
            a= str(x['comment'])
            b= str(x["id"])
            return [a,b]
            # return[b]



