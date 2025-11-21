import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_adminCreateJolt():
    payload = {
      "name": "pytest",
      "sourceType": "string",
      "targetType": "string",
      "joltSpec": "string"
    }
    search_term = f"{endpoint}/admin/joltSpecifications"
    request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminModifyJolt():
    payload = {
      "name": "pytest",
      "sourceType": "string",
      "targetType": "string",
      "joltSpec": "string"
    }
    search_term = f"{endpoint}/admin/joltSpecifications"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminGetJolt():
    search_term = f"{endpoint}/admin/joltSpecifications"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminImportJolt():
    payload = {
      "replace": True,
      "isReplace": False,
      "entities": [
        {
          "name": "pytest",
          "sourceType": "string",
          "targetType": "string",
          "joltSpec": "string"
        }
      ]
    }
    search_term = f"{endpoint}/admin/joltSpecifications/import"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminDeleteJolt():
    joltName = "pytest"
    search_term = f"{endpoint}/admin/joltSpecifications/{joltName}"
    request = requests.delete(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204