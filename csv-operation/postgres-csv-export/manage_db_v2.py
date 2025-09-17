import psycopg2
from psycopg2 import connect, extensions, sql


class ManageDatabase:
    def __init__(self):
        pass

    def database_connection(self, db_name, db_user, db_password, db_host):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        try:
            db_connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port="5432",
            )
            autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
            db_connection.set_isolation_level(autocommit)
            return db_connection
        except (Exception, psycopg2.Error) as error:
            return error