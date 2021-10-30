from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from mysql import connector
from msqlConnection import connecting 
conn = connecting.conn()
mycursor = conn.cursor()
excutable = conn.cursor(dictionary=True)
import webbrowser
import time

class cGatherId:
      def gatherId(self,browser,search:str,searchId):
          chrome = browser
          print("gatherId")
          print("search:"+ search)
          print("searchId:"+ searchId)
          browser = browser
          
          time.sleep(10)
          find_serial = browser.find_element(By.CSS_SELECTOR,"[placeholder='Search']")
          find_serial.send_keys(search)
          time.sleep(5)
          print("type search")
          find_serial = browser.find_element(By.CSS_SELECTOR,".fuqBx div:first-child a")
          find_serial.click()
          time.sleep(10)
          print("click search")
          #######################################################################
          SCROLL_PAUSE_TIME = 5
          counter = 3
          i=0

          # Get scroll height
          last_height = browser.execute_script("return document.body.scrollHeight")
          print("last_height")
          print(last_height)
          while True:
              if(i<=counter):  
                print("inscoll while")
                print("document.body.scrollHeight")
                # Scroll down to bottom
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = browser.execute_script("return document.body.scrollHeight")
                print("new_height")
                print(new_height)
                if new_height == last_height:
                    break
                last_height = new_height
              else:
                break
              i = i+1  
          ##########################################################################
          find_serialx = browser.find_elements_by_css_selector(".Nnq7C.weEfm .v1Nh3.kIKUG._bz0w a")
          try:
            print("find_serialx"+str(len(find_serialx)))
          except:
            print("nolen")   
          try:
            print("intry")
            for e in find_serialx:
              print("infor")
              print(e.get_attribute('href'))
              url = str(e.get_attribute('href'))
              try:
                sql = "INSERT INTO urls (url,description,search_id) VALUES (%s, %s , %s)"
                val = (url, "posts",searchId)
                mycursor.execute(sql, val)
                conn.commit()
                print(mycursor.rowcount, "record inserted.")
              except:
                print("coudent save")  
          except:
            print("cant for")
         
          print("we add first posts in your search term")
          print("we need add pages. wait till thats be done")
          self.addPageAddress(self,chrome,searchId)
     
            
      def addPageAddress(self,browser,searchId=0):
        browser = browser
        time.sleep(10)
        # browser.get("https://www.instagram.com/p/CTsHtjMIvQ2/") 
        # time.sleep(10)
        print("in addPageAddress function")
      
        sql = "Select * from `urls` where(description = 'posts' and (belongs_to = '' or `belongs_to` IS NULL))"
        excutable.execute(sql)
        myresult = excutable.fetchall()
        for x in myresult: 
             print("id:"+str(x['id'])+" - url:"+str(x['url'])+" - description:"+str(x['description'])+ "search_id:"+str(x['search_id']))            
             try:
                print(x)
                post_url = str(x['url'])
                print("post_url:"+ str(post_url))
                print("post_id:")
                print(str(x['id']))
                post_id= x['id']
                print(str(post_id))
                print("searchId:")
                print(str(x['search_id']))
                searchId = x['search_id']
                try: 
                  browser.get(post_url)
                  print("get browser new address")
                  time.sleep(10)
                  find_serial = browser.find_element_by_css_selector(".sqdOP.yWX7d._8A5w5.ZIAjV:first-child")
                  newurl = str(find_serial.get_attribute('href'))
                  sql = "UPDATE urls SET belongs_to = %s WHERE id = %s"
                  val = (newurl, post_id)
                  mycursor.execute(sql, val)
                  conn.commit()
                  print(mycursor.rowcount, "record(s) affected")
                except:
                  print("couldent open url in browser") 
               
             except:
                print("not array")
  
             try:
                print("in add pages try")
                newurl=newurl
                sql = "INSERT INTO urls (url,description,searchId) VALUES (%s, %s,%s)"
                val = (newurl, "pages",searchId)
                mycursor.execute(sql, val)
                conn.commit()
                print(mycursor.rowcount, "record inserted.")
             except connector.Error as err:
                print("coudent save{}".format(err)) 
                            
             try:
                print("post_id")
                print(post_id) 
                print("before update")
                sqls = "UPDATE last_url_with_page SET url_id = {} WHERE url_with_page_id = 1".format(post_id)
                print(sqls)
                mycursor.execute(sqls)
                conn.commit()
                print (sqls)
                print(mycursor.rowcount, "record(s) affected sec")  
             except connector.Error as err:
                print("Something went wrong: {}".format(err))        
