from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from mysql import connector
from pySqlconn import connecting
import webbrowser
import time
mydb = connecting.conn()
excutable = mydb.cursor(dictionary=True)

class instaBotOptions():
    def users_list():
        sql = "SELECT * FROM `options`"
        excutable.execute(sql)
        users = excutable.fetchall()
        for user in users:            
            print("id:")
            print(user["option_id"])
            print("owner_insta_user:")
            print(user["owner_insta_user"])
            print("owner_insta_pass:")
            print(user["owner_insta_pass"])
            print("------------------")
            print("next user")
            print("-------------------")

    def add_user(user,password):
        sql = "INSERT INTO `options` (owner_insta_user,owner_insta_pass) VALUES (%s, %s)"
        val = (user, password)
        excutable.execute(sql, val)
        mydb.commit()
        print(excutable.rowcount, "record inserted.")


    def set_user(id):
        sql = "SELECT * FROM `options` where option_id = {} LIMIT 1".format(id)
        val = id
        excutable.execute(sql, val)
        users = excutable.fetchall()
        user = users[0]
        return [user["owner_insta_user"],user["owner_insta_pass"]]




