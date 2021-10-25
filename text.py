from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from mysql import connector
mydb = connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_instabot"
)
mycursor = mydb.cursor()
import webbrowser
import time

class InstaBot:
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
        time.sleep(10) # Delay for 1 minute (60 seconds).
        print("10 sec pass")
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
   
        # find_serial = browser.find_element_by_css_selector("section.ltpMr.Slqrh span:first-child button.wpO6b")
        # find_serial.click()
        # print("like clicked")
        # time.sleep(2)
      def gatherIds(self,search:str):
          browser = self.browser
          time.sleep(10)
          find_serial = browser.find_element(By.CSS_SELECTOR,"[placeholder='Search']")
          find_serial.send_keys(search)
          time.sleep(5)
          print("type search")
          find_serial = browser.find_element(By.CSS_SELECTOR,".fuqBx div:first-child a")
          find_serial.click()
          time.sleep(10)
          print("click search")
          # find_serial = browser.find_element_by_css_selector(".v1Nh3.kIKUG._bz0w:first-child a")
          # newurl = str(find_serial.get_attribute('href'))
          # time.sleep(5)
          # print(find_serial.get_attribute('href'))
          # browser.get(newurl)
          # print("post clicked")
          # time.sleep(10)
          # print("10 sec pass")
          # find_serialx = browser.find_elements_by_css_selector(".Nnq7C.weEfm")
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

  

  
 


