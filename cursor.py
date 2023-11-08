import mysql.connector

mydb = mysql.connector(
    host="localhost",
    user="root",
    passwd=""
)

my_cursor = mydb.cursor()

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)