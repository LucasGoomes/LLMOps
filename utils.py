import os
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials


def authenticate():
    credentials = Credentials.from_service_account_file(
        filename="key.json",
        scopes=['https://www.googleapis.com/auth/cloud-platform'])

    if credentials.expired:
        credentials.refresh(Request())

    # Set project ID according to environment variable
    PROJECT_ID = os.getenv('PROJECT_ID')

    return credentials, PROJECT_ID
