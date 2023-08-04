FROM python:3.8

RUN pip install mysql-connector-python

COPY ./server /usr/app/src/python

CMD ["python3","./Database.py"]
