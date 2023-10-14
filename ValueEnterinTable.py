import mysql.connector as myconn

def EnterValue(name: str,roll: int):
    db = myconn.connect(host = 'localhost', user='root',passwd = 'redhat',database='abhijitwithai')

    cursorObject = db.cursor()

    struc = 'insert into emp(name,roll) values ( %s , %s)'
    val=(name,roll)

    cursorObject.execute(struc,val)
    db.commit()
    db.close()