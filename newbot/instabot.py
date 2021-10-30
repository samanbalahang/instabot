from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from mysql import connector
from pySqlconn import connecting
from options import instaBotOptions
from searchInsta import cSeachTerms
import webbrowser
import time
mydb = connecting.conn()
mycursor = mydb.cursor()

"""
--------------------------------------------
|
|           USER MANAGE 
|        
|-------------------------------------------
"""
# set user 
# set user from the bank (you should add user befor this for find user id go to finding user id part)
# un comment next lins for set user
##
insta_user = instaBotOptions.set_user(2)
user_name = insta_user[0]
user_pass = insta_user[1]
##

# list of users
##
# instaBotOptions.users_list()

# add user
# if you want add multy user we dont supotrt that but you can add them one by one after add
# - first user & password run theapp affter successfully add user stop runing app and change user
# - and password and do same thin till all users be added
##
# userName = "test"
# password = "test"
# instaBotOptions.add_user(userName,password)




"""
--------------------------------------------
|
|      searching and gathering post id
|       to database
|        
|-------------------------------------------
"""
#add your search terms in search part and short description on desc part 
# search = cSeachTerms(
#      [
#     {"serch": "#احمد_کلاته" , "desc": "رشد پیچ"},
#     {"serch": "#رشد_پیج" , "desc": "رشد پیج"},
#     {"serch": "#تولید_محتوا" , "desc": "رشد پیج"},
#     ],
#     user_name,
#     user_pass
# )
 

# print(user_pass)
# sql = "INSERT INTO urls (url,description) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
