import os
import logging
import csv
from dotenv import load_dotenv
from manage_db_v2 import ManageDatabase
from psycopg2 import OperationalError, DatabaseError
import pandas as pd

#to get to ensure from .env
load_dotenv(override=True)



# getting data from env
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_host=os.getenv("DB_HOST")

csv_output_path="YourTable.csv"

db_con = ManageDatabase().database_connection(
    db_name, db_user, db_password, db_host
    )

def export_csv()->list:
    try:
        cursor = db_con.cursor()
        # select_query = """ 
        #                 SELECT  
        #                 *,
        #                 NOW()  AS "createdAt",
        #                 NOW()  AS "updatedAt"
        #                 FROM "YourTable";
        #                 """
        select_query = """ 
                        SELECT  
                        *
                        FROM "YourTable";
                        """
        cursor.execute(select_query)
        data = cursor.fetchall()
        # Extract column names from cursor.description
        columns = [desc[0] for desc in cursor.description]
        print("data",data)
        print("column",columns)
        df = pd.DataFrame(data)
        df = pd.DataFrame(data, columns=columns)
        print("df",df)
        csv_filename = csv_output_path
        df.to_csv(csv_filename, index=False,quoting=csv.QUOTE_ALL,quotechar='"',date_format='%Y-%m-%d %H:%M:%S')
        return data
    except OperationalError as oe:
        logging.error("Operational error during export: %s", oe)
        db_con.rollback()
        return []
    except DatabaseError as de:
        logging.error("Database error during export: %s", de)
        db_con.rollback()
        return []
    except Exception as e:
        print(e)
        logging.exception("Unexpected error during export")
        return []


def main():
    export_csv()

if __name__=="__main__":
    main()
