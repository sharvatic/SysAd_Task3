import os
import socket


s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect(("localhost", 1234))

file = open("New.txt" , "rb")
size = os.path.getsize("New.txt")

s.send("New_new.txt".encode())
s.send("###".encode())
s.send(str(size).encode())
s.send("###".encode())

data = file.read()
s.sendall(data)
s.send("###".encode())

file.close()

uname = input("Enter your username ")
passwd = input("Enter your password ")

s.send(bytes(uname , ("utf-8")))
s.send(bytes(passwd , ("utf-8")))

p1 = input("Enter the path of the file you want to upload ")
s.send(bytes(p1 , ("utf-8")))

in1 = input("Do you want to extract any files [Y/N]")
s.send(bytes(in1 , ("utf-8")))
if in1 == 'Y' :
    path = input("Provide the path of the folder that you want to extract your files in")
    s.send(bytes(path , ("utf-8")))


else:
    print("Okay")

s.close()
