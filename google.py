import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

root = "https://www.google.com/"
url = "https://google.com/search?q="

query = 'Why do I only see the first 4 results?'  # Fill in google query
query = urllib.parse.quote_plus(query)
link = url + query

print(f'Main link to search for: {link}')

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path='/snap/bin/chromium.chromedriver')
driver.get(link)

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class = "g"]')))
headings = driver.find_elements_by_xpath('//div[@class = "g"]')  # Heading elements

for heading in headings:

    title = heading.find_elements_by_tag_name('h3')
    links = heading.find_element_by_css_selector('.yuRUbf>a').get_attribute("href")  # This ain't working either, any help?
    print(links)
    # link = heading.find_element_by_name('a href')
    for t in title:
        print('title:', t.text)