from peewee import *
from . import config
db = MySQLDatabase(host=config.host, user=config.dbuser, password=config.dbpassword, database=config.dbname)

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField()
    auth_key = CharField()
    email = CharField(default=None)

class Bill(BaseModel):
    # Amount, in dollars
    amount = DoubleField()
    # UNIX timestamp
    time = IntegerField()
    # Username of bill creator
    creator = CharField()
    # ForeignKeyField
    user = ForeignKeyField(User, related_name='bills')
