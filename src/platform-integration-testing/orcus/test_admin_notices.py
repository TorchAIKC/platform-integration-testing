import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def getPytestNoticeID():
    search_term = f"{endpoint}/admin/notices"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    for each in request.json():
        if each['title'] == "pytest":
            return each["id"]

def test_adminCreateNotice():
    payload = {
      "id": "",
      "faIcon": "string",
      "title": "pytest",
      "message": "string",
      "roles": [
        "string"
      ]
    }
    search_term = f"{endpoint}/admin/notices"
    request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200
    
def test_adminModifyNotice():
    payload = {
      "id": getPytestNoticeID(),
      "faIcon": "string",
      "title": "pytest",
      "message": "string",
      "roles": [
        "string"
      ]
    }
    search_term = f"{endpoint}/admin/notices"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminImportNotice():
    payload = {
      "replace": True,
      "isReplace": False,
      "entities": [
        {
          "id": getPytestNoticeID(),
          "faIcon": "string",
          "title": "pytest",
          "message": "string",
          "roles": [
            "string"
          ]
        }
      ]
    }
    search_term = f"{endpoint}/admin/notices/import"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminGetNotices():
    search_term = f"{endpoint}/admin/notices"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminDeletNotice():
    search_term = f"{endpoint}/admin/notices/{getPytestNoticeID()}"
    request = requests.delete(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204