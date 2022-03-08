from sqlalchemy import BigInteger, Column, Float, TIMESTAMP
from sqlalchemy.types import Integer, Numeric, String
from sqlalchemy.dialects.postgresql import JSON
base_schema = {
    "integer_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "timestamp": Column(TIMESTAMP, primary_key=True),
        "source": Column(String, primary_key=True),
        "value": Column(Integer),
        "unit": Column(String),
        "confidence": Column(String, default=None)
        },
    "numeric_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "timestamp": Column(TIMESTAMP, primary_key=True),
        "source": Column(String, primary_key=True),
        "value": Column(Float),
        "unit": Column(String),
        "confidence": Column(String, default=None)
        },
    "string_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "timestamp": Column(TIMESTAMP, primary_key=True),
        "source": Column(String, primary_key=True),
        "value": Column(String),
        "unit": Column(String),
        "confidence": Column(String, default=None)
        },
    "event_schema.avsc": {
        "user_id": Column(String, primary_key=True),
        "start_time": Column(TIMESTAMP, primary_key=True),
        "end_time": Column(TIMESTAMP, primary_key=True),
        "event_name": Column(String, primary_key=True),
        "source": Column(String, primary_key=True),
        "parameters": Column(JSON, primary_key=True)
        }
}