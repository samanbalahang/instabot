from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from mysql import connector
import webbrowser
import time

class cGatherId:
       def gatherId(self,browser,search:str):
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

          # Get scroll height
          last_height = browser.execute_script("return document.body.scrollHeight")
          print("last_height")
          print(last_height)
          while True:
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
          ##########################################################################
          find_serialx = browser.find_elements_by_css_selector(".Nnq7C.weEfm .v1Nh3.kIKUG._bz0w a")
          try:
            print(len(find_serialx))
          except:
            print("nolen")   
          try:
            print("intry")
            for e in find_serialx:
              print("infor")
              print(e.get_attribute('href'))
              url = str(e.get_attribute('href'))
              try:
                sql = "INSERT INTO urls (url,description) VALUES (%s, %s)"
                val = (url, "posts")
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")
              except:
                print("coudent save")  
          except:
            print("cant for")

          try:
            thelinks = find_serialx.find_elements_by_tag_name("a")
            newurl = str(thelinks.get_attribute('href'))
            print(newurl)
            time.sleep(5)
          except:
            print("noselector")  

  

  
 


