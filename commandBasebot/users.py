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