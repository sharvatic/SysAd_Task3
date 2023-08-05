Run the following commands as root user to get the following files
```
cd /
mkdir python
cd python
git clone https://github.com/sharvatic/SysAd_Task3.git
```
Download the python extension in VScode. Install MySQL and install the mysql connector using
```
pip install mysql-connector-python
```
Run the Database.py first and then Login.py using
```
python3 file_name.py
```
Run the server.py and client.py in 2 different instances of the terminal
Buld the dockerfile using 
```
docker build -t python:1.0 .
```
Run the docker container using
```
docker run -itd -p 8080:80 --name file_server python:1.0
```
Run the docker-compose file using 
```
docker compose up
```
