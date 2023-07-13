FROM python:latest

RUN pip install mysql-connector-python

COPY ./Database.py /usr/app/src/Database.py
