from peewee import *
from db import pg_db
from playhouse.postgres_ext import DateTimeTZField, ArrayField


class BaseModel(Model):
    class Meta:
        database = pg_db

class RussianSubscriptions(BaseModel):
    id = AutoField(column_name="id", primary_key=True)
    name = CharField(column_name="name", max_length=255)
    logo = CharField(column_name="logo", max_length=255)
    description = TextField(column_name="description")
    provider_url = TextField(column_name="provider_url")
    created_at = DateTimeTZField(column_name="created_at")

    class Meta:
        table_name = 'russian_subscriptions'

class UserRussianSubscriptions(BaseModel):
    id = AutoField(column_name="id", primary_key=True)
    subscription = ForeignKeyField(column_name="subscription_id", model=RussianSubscriptions)
    price = IntegerField(column_name="price")
    start_date = DateField(column_name="start_date")
    expiration_date = DateField(column_name="expiration_date")
    periodity = IntegerField(column_name="periodity")  # периодичность
    created_at = DateTimeTZField(column_name="created_at")

    class Meta:
        table_name = 'user_russian_subscriptions'

class ForeignSubscriptions(BaseModel):
    id = AutoField(column_name="id", primary_key=True)
    name = CharField(column_name="name", max_length=255)
    logo = CharField(column_name="logo", max_length=255)
    description = TextField(column_name="description")
    plans = ArrayField()
    periodities = ArrayField()
    created_at = DateTimeTZField(column_name="created_at")

    class Meta:
        table_name = 'foreign_subscriptions'

class UserForeignSubscription(BaseModel):
    id = AutoField(column_name="id", primary_key=True)
    subscription = ForeignKeyField(column_name="subscription_id", model=ForeignSubscriptions)
    plan = IntegerField(column_name="plan")
    periodity = IntegerField(column_name="periodity") #периодичность
    price = FloatField(column_name="price")
    start_date = DateField(column_name="start_date")
    expiration_date = DateField(column_name="expiration_date")
    activation_code = TextField(column_name="activation_code")
    auto_renewal = BooleanField(default=False)
    created_at = DateTimeTZField(column_name="created_at")

    class Meta:
        table_name = 'user_foreign_subscriptions'
