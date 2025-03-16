import pymysql
import datetime,json

db_host="127.0.0.1"
db_user="dbadmin"
db_password="Abc123Abc123"
db_name="csv_export_test"

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

def mysql_to_json():
    sql_file = r"D:\python-servers\python-playground\csv-operation\mysql-csv-export\sample_sql_script.sql"
    with open(sql_file) as f:
        sql_queries = f.read()
    print(f"{date_time}>>>sql read data",sql_queries)
    cursor = db_connection.cursor()
    print(f"{date_time}>>db_cursor",cursor)
    cursor.execute(sql_queries)
    data = cursor.fetchall()
    print(f"{date_time}>>rows",data)
    with open(f"output_data.json", "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4, cls=DateTimeEncoder)
    """ 
    columns = [desc[0] for desc in cursor.description]  # Column names
    print(f"{date_time}>>columl",columns)
    with open(f"output_origin_package.csv", "w", newline="", encoding="utf-8") as csvfile:
        fields = columns
        csv_writer = csv.DictWriter(csvfile,fieldnames=fields,quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data) 
    """
    print(f"{date_time}>>Data has been exported to json file.")
    result = {"status":"success"}
    return result



# Custom JSON encoder for datetime
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()  # Convert datetime to ISO 8601 string format
        return super().default(obj)

mysql_to_json()