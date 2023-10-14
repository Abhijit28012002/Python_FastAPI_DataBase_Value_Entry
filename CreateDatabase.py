import mysql.connector as myconn

db = myconn.connect(host = 'localhost', user='root',passwd = 'redhat')
print(db)
print("Database connection establish.......")
cursorObject = db.cursor()

# Create database
cursorObject.execute('CREATE DATABASE ABHIJITWITHAI')
print("Database Creating successfull...")

db.close()