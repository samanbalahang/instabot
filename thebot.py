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



browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://www.instagram.com/accounts/login/")
browser.maximize_window()
# url = 'https://www.instagram.com/accounts/login/'  
# chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(chrome_path).open(url)
find_serial = browser.find_element_by_css_selector("[name='username']")
find_serial.send_keys("cobco_perfume_ca")
find_serial = browser.find_element_by_css_selector("[name='password']")
find_serial.send_keys("perfumec0rp0ratio")
find_serial = browser.find_element_by_css_selector("[type='submit']")
find_serial.click()
clickurl = str("https://www.instagram.com/accounts/onetap/?next=%2F")

while (browser.current_url != clickurl):
    time.sleep(10) # Delay for 1 minute (60 seconds).
    print("10 sec pass")
print ("while ended")
find_serial = browser.find_element_by_css_selector(".sqdOP.L3NKy.y3zKF")
find_serial.click()
time.sleep(2)
find_serial = browser.find_element_by_css_selector(".aOOlW.bIiDR")
find_serial.click()
time.sleep(2)
find_serial = browser.find_element_by_css_selector("[placeholder='Search']")
find_serial.send_keys("#احمد_کلاته")
time.sleep(5)
print("type search")
find_serial = browser.find_element_by_css_selector(".fuqBx div:first-child a")
find_serial.click()
time.sleep(10)
print("click search")
find_serial = browser.find_element_by_css_selector(".v1Nh3.kIKUG._bz0w:first-child a")
newurl = str(find_serial.get_attribute('href'))
time.sleep(5)
print(find_serial.get_attribute('href'))
browser.get(newurl)
print("post clicked")
time.sleep(10)
print("10 sec pass")
find_serial = browser.find_element_by_css_selector("section.ltpMr.Slqrh span:first-child button.wpO6b")
find_serial.click()
print("like clicked")
time.sleep(2)







