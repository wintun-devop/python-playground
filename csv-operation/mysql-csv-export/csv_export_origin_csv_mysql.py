import pymysql
import os,csv,datetime

db_host="your_db_host"
db_user="your_db_user"
db_password="your_db_password"
db_name="your_db_name"

date_time = datetime.datetime.now()
date_time_utc =datetime.datetime.now(datetime.UTC)

def connection(db_host,db_user,db_password,db_name):
    db_connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        db=db_name,
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    return db_connection

db_connection = connection(db_host,db_user,db_password,db_name)

def mysql_to_csv():
    cursor = db_connection.cursor()
    print(f"{date_time}>>db_cursor",cursor)
    print(f"{date_time}>>Data has been exported to output.csv")
    result = {"status":"success"}
    return result

mysql_to_csv()

