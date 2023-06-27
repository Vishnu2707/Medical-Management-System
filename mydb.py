import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Vishnu27*7'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a DB

cursorObject.execute("CREATE DATABASE data")

print("ALL DONE!!")