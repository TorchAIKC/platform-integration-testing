import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_getAllConfigs():
    search_term = f"{endpoint}/admin/config"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_createConfig():
    payload = {
      "name": "pytest",
      "prestoURL": "string",
      "prestoSource": "string",
      "s3URL": "string",
      "s3Region": "string",
      "s3PathStyleAccess": True,
      "graphiteEnabled": True,
      "graphiteUrl": "string",
      "appTitle": "string",
      "appSubtitle": "string",
      "prestoCompressionEnabled": True,
      "soloBaseUrl": "string"
    }
    search_term = f"{endpoint}/admin/config"
    request = requests.post(search_term, data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_modifyConfig():
    payload = {
      "name": "pytest",
      "prestoURL": "change",
      "prestoSource": "string",
      "s3URL": "string",
      "s3Region": "string",
      "s3PathStyleAccess": True,
      "graphiteEnabled": True,
      "graphiteUrl": "string",
      "appTitle": "string",
      "appSubtitle": "string",
      "prestoCompressionEnabled": True,
      "soloBaseUrl": "string"
    }
    search_term = f"{endpoint}/admin/config"
    request = requests.put(search_term, data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_importConfig():
    payload = {
      "replace": True,
      "isReplace": True,
      "entities": [
        {
          "name": "pytest",
          "prestoURL": "string",
          "prestoSource": "string",
          "s3URL": "string",
          "s3Region": "string",
          "s3PathStyleAccess": True,
          "graphiteEnabled": True,
          "graphiteUrl": "string",
          "appTitle": "string",
          "appSubtitle": "string",
          "prestoCompressionEnabled": True,
          "soloBaseUrl": "string"
        }
      ]
    }
    search_term = f"{endpoint}/admin/config/import"
    request = requests.put(search_term, data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200
    
def test_getConfig():
    configName = "pytest"
    search_term = f"{endpoint}/admin/config/{configName}"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_deleteConfig():
    payload = {
      "name": "pytest",
      "prestoURL": "string",
      "prestoSource": "string",
      "s3URL": "string",
      "s3Region": "string",
      "s3PathStyleAccess": True,
      "graphiteEnabled": True,
      "graphiteUrl": "string",
      "appTitle": "string",
      "appSubtitle": "string",
      "prestoCompressionEnabled": True,
      "soloBaseUrl": "string"
    }
    configName = "pytest"
    search_term = f"{endpoint}/admin/config/{configName}"
    request = requests.delete(search_term, data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204