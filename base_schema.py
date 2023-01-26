from sqlalchemy import BigInteger, Column, Float, TIMESTAMP
from sqlalchemy.types import Integer, Numeric, String
from sqlalchemy.dialects.postgresql import JSON, UUID
import uuid
from datetime import datetime

base_schema = {
    "integer_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "timestamp": Column(TIMESTAMP, primary_key=True),
        "source": Column(String, primary_key=True),
        "value": Column(Integer),
        "unit": Column(String),
        "confidence": Column(String, default=None)
        },
    "integer_interval_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "start_time": Column(TIMESTAMP, primary_key=True),
        "end_time": Column(TIMESTAMP, primary_key=True),
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
    "numeric_interval_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "start_time": Column(TIMESTAMP, primary_key=True),
        "end_time": Column(TIMESTAMP, primary_key=True),
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
        "parameters": Column(JSON),
        "unique_event_id": Column(UUID(as_uuid=False), default=uuid.uuid4, unique=True)
        },
     "json_object_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "timestamp": Column(TIMESTAMP, primary_key=True),
        "source": Column(String, primary_key=True),
        "value": Column(JSON),
        "unit": Column(String),
        "confidence": Column(String, default=None)
    },
    "location_datastream_schema.avsc": {
        "individual_id": Column(String, primary_key=True),
        "timestamp": Column(TIMESTAMP, primary_key=True),
        "source": Column(String, primary_key=True),
        "unit": Column(String, default=None),
        "confidence": Column(String, default=None),
        "value": Column(JSON)
    },
    "events_metadata_schema": {
        "individual_id": Column(String, primary_key=True),
        "event_type": Column(String, primary_key=True),
        "source": Column(String, primary_key=True),
        "last_updated": Column(TIMESTAMP, default=datetime.utcnow()),
        "last_observed": Column(TIMESTAMP),
        "observed_parameters": Column(JSON),
        "total_occurences": Column(Numeric)
    },
    "datastream_metadata_schema": {
        "individual_id": Column(String, primary_key=True),
        "source": Column(String, primary_key=True),
        "datastream": Column(String, primary_key=True),
        "last_updated": Column(TIMESTAMP, default=datetime.utcnow())
    }
}

# individual_id character varying COLLATE pg_catalog."default" NOT NULL,
#     source character varying COLLATE pg_catalog."default" NOT NULL,
#     datastream character varying COLLATE pg_catalog."default" NOT NULL,
#     last_updated timestamp without time zone,
#     CONSTRAINT user_datastreams_pkey PRIMARY KEY (individual_id, source, datastream)

base_schema_events = {
    
}
