import os
from dotenv import load_dotenv
from manage_db_pymysql import connection

#to get to ensure from .env
load_dotenv(override=True)

# getting data from env
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_host=os.getenv("DB_HOST")


db_connection = connection(db_host,db_user,db_password,db_name)
print("db_connection",db_connection)