import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_adminCreateFlowEnvironments():
    payload = {
      "name": "pytest",
      "displayName": "pytest",
      "baseUrl": "pytest",
      "readTimeoutMs": 0,
      "connectTimeoutMs": 0
    }
    search_term = f"{endpoint}/admin/flowEnvironments"
    request = requests.post(search_term, data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminModifyFlowEnvironments():
    payload = {
        "name": "pytest",
        "displayName": "pytest",
        "baseUrl": "pytest",
        "readTimeoutMs": 0,
        "connectTimeoutMs": 0
    }
    search_term = f"{endpoint}/admin/flowEnvironments"
    request = requests.put(search_term, data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminImportFlowEnvironments():
    payload = {
      "replace": True,
      "isReplace": False,
      "entities": [
        {
          "name": "pytest",
          "displayName": "pytest",
          "baseUrl": "pytest",
          "readTimeoutMs": 0,
          "connectTimeoutMs": 0
        }
      ]
    }
    search_term = f"{endpoint}/admin/flowEnvironments/import"
    request = requests.put(search_term, data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminGetFlowEnvironments():
    search_term = f"{endpoint}/admin/flowEnvironments"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminDeleteFlowEnvironments():
    environmentName = "pytest"
    search_term = f"{endpoint}/admin/flowEnvironments/{environmentName}"
    request = requests.delete(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204