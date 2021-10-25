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

class cInstaLogins:
      def LogIn(self,username,password):
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
        return browser