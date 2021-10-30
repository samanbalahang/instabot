from msqlConnection import connecting 
conn = connecting.conn()
mycursor = conn.cursor()
excutable = conn.cursor(dictionary=True)
class Search:
    def allSearchTerms():
        dsql = "SELECT * FROM `search_terms`"
        excutable.execute(dsql)
        optionsExcute = excutable.fetchall()
        return optionsExcute
    def addSearchTerm(serch_title,search_desc="پیشفرض"):
        sql = "INSERT INTO `search_terms` (`serch_title`, `search_desc`) VALUES (%s , %s)"
        val = (serch_title, search_desc)
        mycursor.execute(sql, val)
        conn.commit() 
        massage = str((mycursor.rowcount, "record inserted."))
        return int(mycursor.rowcount)
    def selectSearchTerm(search_id):
        dsql = "SELECT * FROM `search_terms` WHERE `search_term_id` = '{}' Limit 1".format(search_id) 
        excutable.execute(dsql)
        optionsExcute = excutable.fetchall()
        return optionsExcute    