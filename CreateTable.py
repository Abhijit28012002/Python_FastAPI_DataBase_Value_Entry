import mysql.connector as myconn

db = myconn.connect(host = 'localhost', user='root',passwd = 'redhat',database='abhijitwithai')

cursorObject = db.cursor()

cursorObject.execute('create table emp(name varchar(20),roll int)')
db.close()