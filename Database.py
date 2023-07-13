import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sharv",
  password="sharv123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE File_archives")