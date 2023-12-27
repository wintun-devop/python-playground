import os
from dotenv import load_dotenv
from manage_db_v2 import ManageDatabase

#to get to ensure from .env
load_dotenv(override=True)

# getting data from env
db_name=os.getenv("DB_NAME")
db_user=os.getenv("DB_USER")
db_password=os.getenv("DB_PASSWORD")
db_host=os.getenv("DB_HOST")


db_con = ManageDatabase().database_connection(
    db_name, db_user, db_password, db_host
    )


def create():
    cursor = db_con.cursor()
    insert_query = """INSERT INTO "Product" (name,model_no,description,arrival) VALUES (%s,%s,%s,%s) RETURNING id,name,model_no,description,arrival"""
    record = ('Mikrotik L009UiGS-2HaxD-IN','CRS310-8G+2S+IN','amazing Marvell 98DX226S switch-chip and integrated dual-core ARM CPU can handle the full potential of RouterOS v7.','1/5/2012')
    cursor.execute(insert_query, record)
    data = cursor.fetchone()
    print(data)
    cursor.close()
    db_con.close()
    return data


def get_one(id):
    id = id
    cursor = db_con.cursor()
    select_query = "SELECT  * FROM \"Product\" where id='{id}'".format(id=id)
    cursor.execute(select_query)
    data = cursor.fetchone()
    print(data)
    cursor.close()
    db_con.close()
    return data


def get_all():
    cursor = db_con.cursor()
    select_query = 'SELECT  * FROM \"Product\"'
    cursor.execute(select_query)
    data = cursor.fetchall()
    print(data)
    cursor.close()
    db_con.close()
    return data


def delete(id):
    cursor = db_con.cursor()
    delete_query = "DELETE from \"Product\" where id='{id}'".format(id=id)
    cursor.execute(delete_query)
    data = "delete success"
    print(data)
    cursor.close()
    db_con.close()
    return data


def update(id, update_field, update_value):
    cursor = db_con.cursor()
    update_query = "UPDATE \"Product\" SET {update_field}='{update_value}' where id='{id}' RETURNING id,name,model_no,description,arrival".format(
        update_field=update_field, update_value=update_value, id=id
    )
    cursor.execute(update_query)
    data = cursor.fetchone()
    print(data)
    cursor.close()
    db_con.close()
    return data


# create()
# delete("ecef4f9c-6dab-44b8-acc8-ba1d6fc4c8b2")
# update("ac65afc5-e683-4de9-9b88-c8b3a316b29e","description","This is good product.")
# get_all()
# get_one("59c822f2-85f6-4c2e-92c3-8ef54782e2da")

