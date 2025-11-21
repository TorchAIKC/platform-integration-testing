import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_adminGetDocs():
    search_term = f"{endpoint}/admin/docs"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminCreateDocs():
    payload = {
        "id": "pytest",
        "name": "pytest",
        "category": "pytest",
        "description": "pytest",
        "s3Bucket": "string",
        "s3ObjectKey": "string",
        "s3PreviewObjectKey": "string",
        "docsAllowedRoles": [
        {
          "roleName": "string",
          "id": 0
        }
        ],
        "allowedRoles": [
        "string"
        ]
    }
    search_term = f"{endpoint}/admin/docs"
    request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminModifyDocs():
    payload = {
        "id": "pytest",
        "name": "pytest",
        "category": "pytest",
        "description": "pytest",
        "s3Bucket": "string",
        "s3ObjectKey": "string",
        "s3PreviewObjectKey": "string",
        "docsAllowedRoles": [
        {
          "roleName": "string",
          "id": 0
        }
        ],
        "allowedRoles": [
        "string"
        ]
    }
    search_term = f"{endpoint}/admin/docs"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminImportDocs():
    payload ={
      "replace": True,
      "isReplace": False,
      "entities": [
        {
          "id": "pytest",
          "name": "pytest",
          "category": "pytest",
          "description": "pytest",
          "s3Bucket": "string",
          "s3ObjectKey": "string",
          "s3PreviewObjectKey": "string",
          "docsAllowedRoles": [
            {
              "roleName": "string",
              "id": 0
            }
          ],
          "allowedRoles": [
            "string"
          ]
        }
      ]
    }
    search_term = f"{endpoint}/admin/docs/import"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminDeleteDocs():
    docsID = "pytest"
    search_term = f"{endpoint}/admin/docs/{docsID}"
    request = requests.delete(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204