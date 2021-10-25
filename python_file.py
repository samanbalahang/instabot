# from text import Person

# p1 = Person("John", 36)
# print(p1.myfunc())
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
import webbrowser
import time
from getRandomComment import getrandComments
x= (getrandComments.randComments())

browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.instagram.com/accounts/login/")
browser.maximize_window()
# url = 'https://www.instagram.com/accounts/login/'  
# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(chrome_path).open(url)
find_serial = browser.find_element_by_css_selector("[name='username']")
find_serial.send_keys(x[0])
