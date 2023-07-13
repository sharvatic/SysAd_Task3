FROM python:3.0

RUN pip install mysql-connector-python

COPY ./Database.py /usr/app/src/Database.py
