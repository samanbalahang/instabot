from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from instaLogin import instaLogins
from mysql import connector

mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_instabot"
)
mycursor = mydb.cursor()
excutable = mydb.cursor(dictionary=True)
sql = "UPDATE urls SET belongs_to = %s WHERE id = %s"
val = ('https://www.instagram.com/bari.editor/', 1)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
import time
class PageOfpost:
     def __init__(self,username, password):
        self.username = username
        self.password = password
        print(username)
        print(password)
        print("self:"+self.username)
        print("self:"+self.password)

        browser = webdriver.Chrome("chromedriver.exe")
        browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        browser.maximize_window()
        self.browser = browser
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
        sql = "Select * from `urls` where(description = 'posts' and (belongs_to = '' or `belongs_to` IS NULL))"
        excutable.execute(sql)
        myresult = excutable.fetchall()
        for x in myresult:            
             try:
                 post_url = str(x['url'])
                 print(post_url)
                 post_id= x['id']
                 print(post_id)
             except:
                  print("not array")
             try:     
                browser.get(post_url)
                time.sleep(10)
                find_serial = browser.find_element_by_css_selector(".sqdOP.yWX7d._8A5w5.ZIAjV:first-child")
                newurl = str(find_serial.get_attribute('href'))
                sql = "UPDATE urls SET belongs_to = %s WHERE id = %s"
                val = (newurl, post_id)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record(s) affected")
             except:
                 print("D")   
             try:
                print("post_id")
                print(post_id) 
                sqls = "UPDATE last_url_with_page SET url_id = {} WHERE url_with_page_id = 1".format(post_id)
                vals = ('17')
                mycursor.execute(sqls, vals)
                # mydb.commit()
                # sqls = "UPDATE last_url_with_page SET url_id = 17 WHERE url_with_page_id = 1"
                # vals = (post_id)
                # mycursor.execute(sqls)
                mydb.commit()
                print (sqls)
                print(mycursor.rowcount, "record(s) affected sec")  
             except connector.Error as err:
                print("Something went wrong: {}".format(err))    
             try:
                sql = "INSERT INTO urls (url,description) VALUES (%s, %s)"
                val = (newurl, "pages")
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
             except:
                print("coudent save")  



            


