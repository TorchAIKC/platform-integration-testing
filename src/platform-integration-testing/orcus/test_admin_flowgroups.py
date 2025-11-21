import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_adminCreateFlowGroup():
    payload = {
      "name": "pytest",
      "displayName": "pytest",
      "description": "pytest"
    }
    search_term = f"{endpoint}/admin/flowGroups"
    request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminModifyFlowGroup():
    payload = {
      "name": "pytest",
      "displayName": "pytest",
      "description": "pytest"
    }
    search_term = f"{endpoint}/admin/flowGroups"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminImportFlowGroup():
    payload = {
      "replace": True,
      "isReplace": False,
      "entities": [
        {
          "name": "pytest",
          "displayName": "pytest",
          "description": "pytest"
        }
      ]
    }
    search_term = f"{endpoint}/admin/flowGroups/import"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200
    
def test_adminGetFLowGroups():
    search_term = f"{endpoint}/admin/flowGroups"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200
    
def test_adminDeleteFlowGroup():
    flowID = "pytest"
    search_term = f"{endpoint}/admin/flowGroups/{flowID}"
    request = requests.delete(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204