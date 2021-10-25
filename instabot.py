from selenium import webdriver
import webbrowser


browser = webdriver.Chrome("chromedriver.exe")

# browser.get("https://www.instagram.com/accounts/login/")
# find_serial = browser.find_element_by_css_selector("[name='username']")
# find_serial.send_keys("solace.iran.shop")

url = 'https://www.instagram.com/accounts/login/'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)