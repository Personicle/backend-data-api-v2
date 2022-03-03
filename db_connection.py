import sqlalchemy
import databases
from pydantic import BaseModel
from typing import List, Optional, Text
from datetime import datetime, timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
import traceback
from configparser import ConfigParser

config_object = ConfigParser()
config_object.read("config.ini")
database = config_object["CREDENTIALS_DATABASE"]

logger = logging.getLogger(__name__)

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(database['USERNAME'], database['PASSWORD'],database['HOST'],database['NAME'], 'prefer')
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
# engine = sqlalchemy.create_engine("postgresql://{username}:{password}@{dbhost}/{dbname}".format(username=database['USERNAME'], password=database['PASSWORD'],
#                                                                                                         dbhost=database['HOST'], dbname=database['NAME']))
  
engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
# metadata.create_all(engine)
Base = declarative_base(engine)


def generate_table_class(table_name: str, base_schema: dict):
    try:
        base_schema['__tablename__'] = table_name
        base_schema['__table_args__'] = {'extend_existing': True}
        generated_model = type(table_name, (Base, ), base_schema)
        generated_model.__table__.create(bind=engine, checkfirst=True)
    except Exception as e:
        logger.error(traceback.format_exc())
        generated_model = None
    return generated_model

# pydantic model 
# class HeartRate(BaseModel):
#     individual_id: str
#     timestamp: Optional[datetime]
#     source: str
#     value: int
#     unit: str
#     confidence: float

# heartrates = sqlalchemy.Table(
#    "heartrate",
#     metadata,
#     sqlalchemy.Column("individual_id", sqlalchemy.TEXT, primary_key=True),
#     sqlalchemy.Column("timestamp", sqlalchemy.TIMESTAMP,primary_key=True),
#     sqlalchemy.Column("source", sqlalchemy.TEXT,primary_key=True),
#     sqlalchemy.Column("value", sqlalchemy.INT),
#     sqlalchemy.Column("unit", sqlalchemy.TEXT),
#     sqlalchemy.Column("confidence", sqlalchemy.REAL),
# )