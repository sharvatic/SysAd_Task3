import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sharv",
  password="sharv123",
  database = "File_archives" 
)

mycursor = mydb.cursor()


mycursor.execute("CREATE TABLE IF NOT EXISTS Login (uname VARCHAR(50) NOT NULL, passwd VARCHAR(50) NOT NULL)")

# mycursor.execute("DELETE FROM Login WHERE uname='User3'")
# mycursor.execute("DELETE FROM Login WHERE uname='User1'")
# mycursor.execute("DELETE FROM Login WHERE uname='User2'")

query = "INSERT into Login (uname , passwd) VALUES (%s , %s)"
val = ("User1" , "user1@abc")
val1 = ("User2" , "user2@abc")
val2 = ("User3" , "user3@abc")

mycursor.execute(query, val)
mycursor.execute(query, val1)
mycursor.execute(query, val2)

mydb.commit()

uname = input("Enter your username")
passwd = input("Enter your password")

selquery = ("SELECT * FROM Login WHERE uname = uname")
mycursor.execute(selquery)

result = mycursor.fetchall()

if passwd == result[0][1]:
    print("Login Successful")
else:
    print("Login Unsuccessful")


