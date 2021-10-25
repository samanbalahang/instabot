from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
from selenium.webdriver.common.keys import Keys
from instaLogin import instaLogins
from mysql import connector
from randoms import randompy
from getRandomComment import getrandComments

perday = 1
maxlikes = 680
maxComment = 170
maxfallow = 130 
username = 'cobco_perfume_ca'
password = "perfumec0rp0ratio"



"""
--------------------------------------------
|
|
|       MY SQL CONNECTION 
|-------------------------------------------
"""
mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_instabot"
)
mycursor = mydb.cursor()
excutable = mydb.cursor(dictionary=True)

"""
--------------------------------------------
|
|      get OPtion Id
|       
|-------------------------------------------
"""   
try:
    print("try select options")
    
    # dsql = "SELECT * FROM `options` WHERE `owner_insta_user` = 'cobco_perfume_ca' ORDER BY `owner_insta_user` ASC LIMIT 1"
    dsql = "SELECT * FROM `options` WHERE `owner_insta_user` = '{}' ORDER BY `owner_insta_user` ASC LIMIT 1".format(username)
    vals = (username)
    print("dsql")
    print(dsql)
    excutable.execute(dsql,vals)
    optionsExcute = excutable.fetchall()
    print("optionsExcute")
    print(optionsExcute)
    for item in optionsExcute:
        print("in for OPTION")
        print(item["option_id"])
        print(item["owner_insta_user"])
        print(item["owner_insta_pass"])
        options_id = int(item["option_id"])
except connector.Error as err:
    print("Something went wrong: {}".format(err)) 
    options_id=0   





"""
--------------------------------------------
|
|
|       LOG IN TO INSTAGRAM 
|-------------------------------------------
"""
browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
browser.maximize_window()
find_serial = browser.find_element_by_css_selector("[name='username']")
find_serial.send_keys(username)
find_serial = browser.find_element_by_css_selector("[name='password']")
find_serial.send_keys(password)
find_serial = browser.find_element_by_css_selector("[type='submit']")
find_serial.click()
clickurl = str("https://www.instagram.com/accounts/onetap/?next=%2F")
while (browser.current_url != clickurl):
    time.sleep(10) # Delay for 1 minute (60 seconds).
    print("10 sec pass")
print ("while ended")
find_serial = browser.find_element_by_css_selector(".sqdOP.L3NKy.y3zKF")
find_serial.click()
time.sleep(10)
find_serial = browser.find_element_by_css_selector(".aOOlW.bIiDR")
find_serial.click()
print ("alow btn clicked")

sql = "Select * from urls where(description = 'posts') AND URLS.id NOT IN (Select url_id FROM url_activity)"
excutable.execute(sql)
myresult = excutable.fetchall()

try:
    print("row count")
    print(excutable.rowcount)
except:
    print('lo')




"""
--------------------------------------------
|
|      ADD ACTIVITY TO GATHERING DATA
|       
|-------------------------------------------
"""    

def liking(): 
    print("liking")
    counter = 0
    randit = randompy.funkrandome()
    for x in myresult:
        xId=x['id']
        if counter != randit:
            post_url = str(x['url'])
            print(post_url)
            browser.get(post_url)
            time.sleep(10)
            print("post clicked")
            time.sleep(10)
            print("10 sec pass")
            find_serial = browser.find_element_by_css_selector("section.ltpMr.Slqrh span:first-child button.wpO6b")
            find_serial.click()
            print("like clicked")
            time.sleep(2)

            """
            --------------------------------------------
            |
            |      INSERT TO url_activity
            |       
            |-------------------------------------------
            """  
            activitysql = "INSERT INTO url_activity (option_id,url_id,f_activity_id,comment_id) VALUES (%s, %s,1,0)"
            val = (options_id, xId)
            mycursor.execute(activitysql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            randnum =  randompy.likerandom()
            print("randum")
            print(randnum) 
            sleeping = int(randnum*60)
            print("Sleeping:")
            print(sleeping)     
            time.sleep(sleeping)
            counter += 1
        else:
            counter = 0
            activityChois = randompy.activRandome()
            if activityChois == 1:
                commenting()    
            elif activityChois == 2: 
                following()
            else:
                pousing()    


def commenting():
    print("comment")
    counter = 0
    randit = randompy.funkrandome()
    for x in myresult:
        xId=x['id']
        if counter != randit:
            post_url = str(x['url'])
            print(post_url)
            browser.get(post_url)
            time.sleep(10)
            print("post clicked")
            time.sleep(10)
            print("10 sec pass")
            find_serial = browser.find_element_by_css_selector("section.ltpMr.Slqrh span:nth-child(2) button.wpO6b")
            find_serial.click()
            time.sleep(10)
            print("10 sec pass")
            comments = getrandComments.randComments()
            print("comments")
            print(comments)
            commentId = comments[1]
            print("commentId")
            print(commentId)
            comment  = comments[0]
            print("comments")
            print("comments")
            print(comment)
            find_serial = browser.find_element_by_css_selector("section.sH9wk._JgwE textarea.Ypffh")
            find_serial.send_keys(comment)
            time.sleep(3)
            find_serial = browser.find_element_by_css_selector("section.sH9wk._JgwE button.sqdOP.yWX7d.y3zKF")
            find_serial.click()
            """
            --------------------------------------------
            |
            |      INSERT TO url_activity
            |       
            |-------------------------------------------
            """  
            activitysql = "INSERT INTO url_activity (option_id,url_id,f_activity_id,comment_id) VALUES (%s, %s,2,%s)"
            val = (options_id,xId,commentId)
            mycursor.execute(activitysql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            print("END INSERT TO url_activity")
            randnum =  randompy.commentRandom()
            print("randum")
            print(randnum) 
            sleeping = int(randnum*60)
            print("Sleeping:")
            print(sleeping)     
            time.sleep(sleeping)
            counter += 1
        else:
           counter = 0
           activityChois = randompy.activRandome()
           if activityChois == 1:
                liking()    
           elif activityChois == 2: 
                following()
           else:
                pousing()    

def following():
    counter = 0
    randit = randompy.funkrandome()
    for x in myresult:
        xId=x['id']
        if counter != randit:
            post_url = str(x['url'])
            print(post_url)
            browser.get(post_url)
            time.sleep(10)
            print("post clicked")
            time.sleep(10)
            print("10 sec pass")
            find_serial = browser.find_element_by_css_selector("header.Ppjfr button.sqdOP.yWX7d.y3zKF")
            if find_serial.text == 'Follow':
                find_serial.click()
                time.sleep(10)
                
                """
                --------------------------------------------
                |
                |      INSERT TO url_activity
                |       
                |-------------------------------------------
                """  
                activitysql = "INSERT INTO url_activity (option_id,url_id,f_activity_id,comment_id) VALUES (%s, %s,3,0)"
                val = (options_id,xId)
                mycursor.execute(activitysql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
                print("END INSERT TO url_activity")
            randnum =  randompy.commentRandom()
            print("randum")
            print(randnum) 
            randnum =  randompy.followingRandom()
            print("randum")
            print(randnum) 
            sleeping = int(randnum*60)
            print("Sleeping:")
            print(sleeping)     
            time.sleep(sleeping)
            counter += 1
        else:
           counter = 0
           activityChois = randompy.activRandome()
           if activityChois == 1:
                liking()    
           elif activityChois == 2: 
                commenting()
           else:
                pousing()    
def pousing():
     sleeping =  int(randompy.pousingRandoum())
     time.sleep(sleeping)
     activityChois = randompy.activRandome()
     if activityChois == 1:
        liking()    
     elif activityChois == 2: 
        commenting()
     else:
        following()  

    
        
liking()  
