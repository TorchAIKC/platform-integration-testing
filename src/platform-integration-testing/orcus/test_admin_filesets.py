import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_adminGetAllFilesets():
    search_term = f"{endpoint}/admin/filesets"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminCreateFileset():
    payload = {
      "id": "pytest",
      "description": "pytest",
      "s3Bucket": "string",
      "s3Prefix": "string",
      "allowedRoles": [
        {
          "roleName": "string",
          "id": 0
        }
      ],
      "enabled": True,
      "allowsUploads": True,
      "alowsUploads": True
    }
    search_term = f"{endpoint}/admin/filesets"
    request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminModifyFileset():
    payload = {
      "id": "pytest",
      "description": "pytest",
      "s3Bucket": "string",
      "s3Prefix": "string",
      "allowedRoles": [
        {
          "roleName": "string",
          "id": 0
        }
      ],
      "enabled": True,
      "allowsUploads": True,
      "alowsUploads": True
    }
    search_term = f"{endpoint}/admin/filesets"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminImportFileset():
    payload = {
      "replace": True,
      "isReplace": False,
      "entities": [
        {
          "id": "pytest",
          "description": "pytest",
          "s3Bucket": "string",
          "s3Prefix": "string",
          "allowedRoles": [
            {
              "roleName": "string",
              "id": 0
            }
          ],
          "enabled": True,
          "allowsUploads": True,
          "alowsUploads": True
        }
      ]
    }
    search_term = f"{endpoint}/admin/filesets/import"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminGetFileset():
    filesetID = "pytest"
    search_term = f"{endpoint}/admin/filesets/{filesetID}"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminDisableFileset():
    filesetID = "pytest"
    search_term = f"{endpoint}/admin/filesets/{filesetID}/disable"
    request = requests.put(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200
    
def test_adminEnableFileset():
    filesetID = "pytest"
    search_term = f"{endpoint}/admin/filesets/{filesetID}/enable"
    request = requests.put(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminDeleteFileset():
    filesetID = "pytest"
    search_term = f"{endpoint}/admin/filesets/{filesetID}"
    request = requests.delete(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204

