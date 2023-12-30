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

#create 
def create():
    cursor = db_connection.cursor()
    id='uuidv4()'
    name = 'Mikrotik CME Gateway'
    model_no='CME22-2n-BG7-Test6'
    description='wireless usage.'
    arrival = '1/7/2012'
    insert_query = f"INSERT INTO product (id,name,model_no,description,arrival) VALUES ({id},'{name}','{model_no}','{description}','{arrival}')"
    cursor.execute(insert_query)
    result = str(cursor.lastrowid)
    print(result)
    cursor.close()
    db_connection.close()
    return result

#read
def get_one(id):
    cursor = db_connection.cursor()
    select_query = "SELECT  * FROM product where id='{id}'".format(id=id)
    cursor.execute(select_query)
    data = cursor.fetchone()
    print(data)
    cursor.close()
    db_connection.close()
    return data

def get_all():
    cursor = db_connection.cursor()
    select_query = "SELECT  * FROM product"
    cursor.execute(select_query)
    data = cursor.fetchall()
    print(data)
    cursor.close()
    db_connection.close()
    return data

#update
def update(id, update_field, update_value):
    cursor = db_connection.cursor()
    update_query = "UPDATE product SET {update_field}='{update_value}' where id='{id}'".format(
        update_field=update_field, update_value=update_value, id=id
    )
    cursor.execute(update_query)
    cursor.execute("SELECT  * FROM product where id='{id}'".format(id=id))
    data=cursor.fetchone()
    print(data)
    cursor.close()
    db_connection.close()
    return data


#delete
def delete(id):
    cursor = db_connection.cursor()
    delete_query = "DELETE from product where id='{id}'".format(id=id)
    cursor.execute(delete_query)
    data = "delete success"
    print(data)
    cursor.close()
    db_connection.close()
    return data

# create()
# get_one("c4402b11-d9f7-44bf-8466-7dd26b50e475")
# get_all()
# delete("19623a68-8f77-4420-8fee-ab3123a42f3a")
#update("1915b9bd-2fda-41c9-90a1-b5ad071b8a05","description","wireless usage update 3")