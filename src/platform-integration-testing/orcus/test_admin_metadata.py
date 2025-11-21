import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_adminGetMetaData():  
    search_term = f"{endpoint}/admin/metadata"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200