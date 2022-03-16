import os
from configparser import ConfigParser

if os.environ.get('DEV_ENVIRONMENT', 'LOCAL') in ["PRODUCTION", "AZURE_STAGING"]:
    DB_CONFIG = {
        "USERNAME": os.environ["DB_USERNAME"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "NAME": os.environ["DB_NAME"]
    }

    OKTA_CONFIG={
        "CLIENT_ID": os.environ["OKTA_CLIENT_ID"],
        "CLIENT_SECRET": os.environ["OKTA_CLIENT_SECRET"],
        "ISSUER": os.environ["OKTA_ISSUER"],
        "AUDIENCE": os.environ["OKTA_AUDIENCE"]
    }

else:
    config_object = ConfigParser()
    config_object.read("config.ini")
    DB_CONFIG = config_object["CREDENTIALS_DATABASE"]
    OKTA_CONFIG = config_object["OKTA"]