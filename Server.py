import socket

from zipfile import ZipFile

import mysql.connector

mydb = mysql.connector.connect( 
    host = "localhost", 
    user = "sharv", 
    passwd = "sharv123", 
    database = "File_archives" 
) 
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Files (uname VARCHAR(50), file LONGBLOB)")



def Addfile(uname , fname):
    query = ("INSERT into Files (uname , file) Values (%s , %s)")

    f = ZipFile('file1.zip' , 'w')
    f.write(fname)

    data = f.read(fname)

    val = (uname , data)

    mycursor.execute(query , val)

    mydb.commit()
    f.close()


def Extractfile(uname , path):
    selquery = ("SELECT * FROM Files WHERE uname = uname")
    mycursor.execute(selquery)

    result = mycursor.fetchall()
    i = 0
    for row in result:
        i = i+1
        fl = open("{i}.txt" , "wb")
        fl.write(row[1])
        fl.close()

        file = ZipFile('New1.zip' , 'w')
        file.write("{i}.txt")
        file.close()

    uf = ZipFile('New1.zip' , 'r')
    uf.extractall(path)

    uf.close()
    







server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(("localhost", 1234))
server.listen()
fname = ""
size = ""
data = ""

client, address = server.accept()

file_name = client.recv(1024).decode()

line = file_name.split("###")
fname = line[0] 
size = line[1]  
data = line[2]

print(fname) 
print(size)
print(data)   

file = open(fname , "wb")

file.write(bytes(data , ("utf-8")))

file.close()

##############################################################################

uname = client.recv(1024)
uname = uname.decode("utf-8")

passwd = client.recv(1024)
passwd = passwd.decode("utf-8")

selquery = ("SELECT * FROM Login WHERE uname = uname")
mycursor.execute(selquery)

result = mycursor.fetchall()

if passwd == result[0][1]:
    str1 = "Login Successful"
    client.send(bytes(str2 , ("utf-8")))
    p1 = client.recv(1024)
    p1 = p1.decode("utf-8")
    Addfile(uname , p1)

else:
    str2 = "Login Unsuccessful"
    client.send(bytes(str1 , ("utf-8")))

in1 = client.recv(1024)
in1 = in1.decode("utf-8")

if in1 == 'Y' :
    path = client.recv(1024)
    path = path.decode("utf-8")
    Extractfile(uname , path)


client.close()
server.close()

