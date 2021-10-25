# instabot
python test.py
python runPageOfPost.py


# database
- we used mysql database you can download in free from 
- [mysql](https://www.mysql.com/downloads/)
- or you can use xampp or wampp or somthing like them we recommended xampp 
- [xampp](https://www.apachefriends.org/download.html)
- # note:
- for this project realy dosent mater what version of xaampp you will install 
ut if you want use xammp for other project use 7.3.*
- # how to use database in xampp:
-  run mysql service in xampp admin panell
- go to this url:
- http://localhost/phpmyadmin
- click on new in the left panell thats show at top of panell 
- name your database python_instabot and create it 
- click on python_instabot in the left panel 
- click on import from top menu and choose python_instabot.sql from downloaded package and you be good to go 
# tables explanation
- options: 
- - is list of users that you wana login with
- urls 
- - keep urls value and a description about it
- comments
- - has all comments 
- comments_cat
- - has all category for comments
- activites
- - has all activities like comment and like
- url_activity
- - keep list of optins(users) & urls and activites
