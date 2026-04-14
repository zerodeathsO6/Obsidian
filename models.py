from peewee import * # type: ignore
from datetime import datetime
db_proxy = Proxy() # This is a placeholder

class BaseModel(Model):
    class Meta:
        database = db_proxy

class Routines(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    routine_content = TextField()
    time = DateTimeField(default=datetime.now)
    # Add whatever else you want to track