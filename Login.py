import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sharv",
  password="sharv123",
  database = "File_archives" 
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS Login (uname VARCHAR(50) NOT NULL, passwd VARCHAR(50) NOT NULL)")

query = "INSERT into Login (uname , passwd) VALUES (%s , %s)"
val = ("User1" , "user1@abc")
val1 = ("User2" , "user2@abc")
val2 = ("User3" , "user3@abc")

mycursor.execute(query, val)
mycursor.execute(query, val1)
mycursor.execute(query, val2)

mydb.commit()
