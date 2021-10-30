from activiteis import activities
from users import users
from LogIn import LogIn
from txtFile import TextFile
from search import Search
from storePostPages import cGatherId
# for each test uncoment it and run it

# test set activities 
# print(activities.selectedActivity(2))


# test set user 
# print(users.addUser('test','test'))
# value = input("Please enter a username or email address:\n")
# password = input("Please enter a password:\n")
# print(users.addUser(value,password))



# test select user 
# print(users.selectUser('solace.iran.shop')[0]["option_id"])


# test update user 
# uId= users.selectUser('test')[0]["option_id"]
# print(users.editUser('edittest','eduitepass',uId))


# test delete user 
# uId= users.selectUser('edittest')[0]["option_id"]
# print(users.delUser(uId))

# test Allusers
Users = users.allusers()
text_file = open("./data.txt", "w")
text_file.write("")
for user in Users:
    text = str(user["option_id"])+" : "+ str(user["owner_insta_user"])
    print(text)
    text_file = open("./data.txt", "a")
    text_file.write(text)
    text_file.write("\n")
text_file.close()
TextFile.openTextFile("./data.txt")


# login 
# uId= users.selectUser('solace.iran.shop')[0]["option_id"]
# user= users.selectUser('solace.iran.shop')[0]["owner_insta_user"]
# password= users.selectUser('solace.iran.shop')[0]["owner_insta_pass"]
# LogIn.LogIn(LogIn,user,password)


#SEARCH TERMS
# allSearchTerm = Search.allSearchTerms()
# for searchTerm in allSearchTerm:
#     # print(str(searchTerm["search_term_id"])+":"+ str(searchTerm["serch_title"]))
#     text_file = open("./data.txt", "w")
#     text_file.write(str(searchTerm["search_term_id"])+":"+ str(searchTerm["serch_title"]))
#     text_file.close()
#     TextFile.openTextFile("./data.txt")

# addSearchTerm
# value = input("Please enter a searchTerm:\n")
# describe = input("Please describe your terms shortly:\n")
# print(Search.addSearchTerm(value,describe))

# selectSearchTerm
# value = input("Please enter a searchTerm ID you will see it in front of search term in txt file:\n")
# searchTermRow = Search.selectSearchTerm(value)
# serchTermTitle = searchTermRow[0]["serch_title"]

#STORE POST PAGE (gatherId)
value = input("Please enter a user id from text file or input 0 for add new user:\n")
if(value != 0):
    TextFile.closetextFile()
    username = users.selectUserById(value)[0]["owner_insta_user"]
    password =  users.selectUserById(value)[0]["owner_insta_pass"]
    print("your user name is :"+ username + " \n your password is :"+ password )
else:
  TextFile.closetextFile()  
  # test add user 
  username = input("Please enter a username or email address:\n")
  password = input("Please enter a password:\n")
  print(users.addUser(username,password))
  value = input("Please enter a username or email address:\n")
  password = input("Please enter a password:\n")
  print(users.addUser(value,password))      

# # selectSearchTerm

allSearchTerm = Search.allSearchTerms()
for searchTerm in allSearchTerm:
    # print(str(searchTerm["search_term_id"])+":"+ str(searchTerm["serch_title"]))
    text_file = open("./data.txt", "w")
    text_file.write(str(searchTerm["search_term_id"])+":"+ str(searchTerm["serch_title"]))
    text_file.close()
    print(str(searchTerm["search_term_id"])+":"+ str(searchTerm["serch_title"]))
    TextFile.openTextFile("./data.txt")
SearchTermId = input("Please enter a searchTerm ID or input 0 for add new one:\n")
if(SearchTermId != 0):
    TextFile.closetextFile()
    searchTermRow = Search.selectSearchTerm(SearchTermId)
    searchTerm = searchTermRow[0]["serch_title"]
else:
   TextFile.closetextFile() 
   # addSearchTerm
   searchTerm = input("Please enter a searchTerm:\n")
   describe = input("Please describe your terms shortly:\n")
   SearchTermId = Search.addSearchTerm(searchTerm,describe)
   

browser =LogIn.LogIn(LogIn,username,password)
cGatherId.gatherId(cGatherId,browser,searchTerm,SearchTermId)


#addPageAddress
# cGatherId.addPageAddress(cGatherId,browser,0)11