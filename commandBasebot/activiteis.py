from msqlConnection import connecting 
conn = connecting.conn()
mycursor = conn.cursor()
excutable = conn.cursor(dictionary=True)
class activities:
    def allActivities():
        dsql = "SELECT * FROM `activites"
        excutable.execute(dsql)
        optionsExcute = excutable.fetchall()
        return optionsExcute
    def selectedActivity(id:int):
        return {
            1: 'first Selected',
            2: 'second Selected',
        }.get(id, 9)
