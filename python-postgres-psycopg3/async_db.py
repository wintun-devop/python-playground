import asyncio
import os
from dotenv import load_dotenv
import psycopg

load_dotenv(override=True)

class AsyncDatabase:
    def __init__(self):
        self.db_name = os.getenv("DB_NAME")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST")
    async def connect(self):
        return await psycopg.AsyncConnection.connect(
            dbname=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port="5432"
        )
