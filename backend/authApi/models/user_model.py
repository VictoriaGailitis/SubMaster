from peewee import *
from db import pg_db
from playhouse.postgres_ext import DateTimeTZField


class BaseModel(Model):
    class Meta:
        database = pg_db

class User(BaseModel):
    id = AutoField(column_name="id", primary_key=True)
    name = CharField(column_name="name", max_length=255)
    email = CharField(column_name="email", max_length=255)
    password = CharField(column_name="password", max_length=255)
    card_number = CharField(max_length=16, null=True)
    created_at = DateTimeTZField(column_name="created_at")

    class Meta:
        table_name = 'users'