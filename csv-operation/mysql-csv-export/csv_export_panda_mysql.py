import pymysql
import os,csv,datetime
import pandas as pd

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
    sql_file = r"D:\python-servers\python-playground\csv-operation\mysql-csv-export\sample_sql_script.sql"
    with open(sql_file) as f:
        sql_queries = f.read()
    print(f"{date_time}>>>sql read data",sql_queries)
    cursor = db_connection.cursor()
    print(f"{date_time}>>db_cursor",cursor)
    cursor.execute(sql_queries)
    data = cursor.fetchall()
    print(f"{date_time}>>rows",data)
    columns = [desc[0] for desc in cursor.description]  # Column names
    print(f"{date_time}>>columl",columns)
    """ 
    with open(f"output_origin_package.csv", "w", newline="", encoding="utf-8") as csvfile:
        fields = columns
        csv_writer = csv.DictWriter(csvfile,fieldnames=fields,quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)
    """
    df = pd.DataFrame(data)
    csv_filename = 'output_pandas_package.csv'
    df.to_csv(csv_filename, index=False,quoting=csv.QUOTE_NONNUMERIC,quotechar='"',date_format='%Y-%m-%d %H:%M:%S')
    print(f"{date_time}>>Data has been exported to output.csv")
    result = {"status":"success"}
    return result

mysql_to_csv()

