import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_getDefault():
    search_term = f"{endpoint}/"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_getLogin():
    search_term = f"{endpoint}/login"
    request = requests.post(search_term,data={'username': username, 'password': password})
    assert request.status_code == 200

### Needs More Testing
# def test_getAuditing():
#     ### Needs more testing
#     search_term = f"{endpoint}/auditing/allowed"
#     request = requests.get(search_term, auth=HTTPBasicAuth(username,password))
#     assert request.status_code == 200

### Needs More Testing
# def test_authRefresh():
#     search_term = f"{endpoint}/auth/refresh"
#     payload = {"refreshToken":""}
#     request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
#     assert request.status_code == 200  