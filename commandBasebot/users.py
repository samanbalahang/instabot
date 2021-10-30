from msqlConnection import connecting
conn = connecting.conn()
mycursor = conn.cursor()
excutable = conn.cursor(dictionary=True)

class users:
    def allusers():
        dsql = "SELECT * FROM `options`"
        excutable.execute(dsql)
        optionsExcute = excutable.fetchall()
        return optionsExcute 
    def addUser(userName,password):
        sql = "INSERT INTO `options` (`owner_insta_user`, `owner_insta_pass`) VALUES (%s , %s)"
        val = (userName, password)
        mycursor.execute(sql, val)
        conn.commit() 
        massage = str((mycursor.rowcount, "record inserted."))
        return massage
    def selectUser(userName): 
        dsql = "SELECT * FROM `options` WHERE `owner_insta_user` = '{}' Limit 1".format(userName) 
        # return dsql
        excutable.execute(dsql)
        optionsExcute = excutable.fetchall()
        return optionsExcute
        for x in optionsExcute:
           xId=x['option_id']
           return xId
    def selectUserById(userId):
        dsql = "SELECT * FROM `options` WHERE `option_id` = '{}' Limit 1".format(userId) 
        excutable.execute(dsql)
        optionsExcute = excutable.fetchall()
        return optionsExcute          
    def editUser(userName,password,userId):
        sql = "UPDATE `options` SET `owner_insta_user` = %s, `owner_insta_pass`=%s WHERE option_id=%s"
        val = (userName, password,userId)
        mycursor.execute(sql, val)
        conn.commit() 
        massage = str((mycursor.rowcount, "record inserted."))
        return massage
    def delUser(userId):
        sql = "DELETE FROM `options` WHERE `option_id`= {} ".format(userId)
        val = (userId)  
        mycursor.execute(sql)
        conn.commit() 
        massage = str((mycursor.rowcount, "record inserted."))
        return massage          