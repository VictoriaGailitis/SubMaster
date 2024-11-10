from playhouse.postgres_ext import PostgresqlExtDatabase
from dotenv import load_dotenv
import os

load_dotenv()

pg_db = PostgresqlExtDatabase(os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"),
                        host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"), autorollback=True)