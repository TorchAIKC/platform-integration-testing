import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_getNotices():
    search_term = f"{endpoint}/notices"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_getNewNotices():
    search_term = f"{endpoint}/notices/new"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

# ### Needs Payload Edits
# def test_getViewedNotices():
#     paylod = {"noticeIds": []}
#     search_term = f"{endpoint}/notices/viewed"
#     request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
#     assert request.status_code == 200

