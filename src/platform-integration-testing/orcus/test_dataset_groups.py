import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("orcus_creds.json") as datafile:
    creds = json.load(datafile)
    endpoint = creds['endpoint']
    my_username = creds['username']
    my_password = creds['password']

def test_getDatasetGroupings():
    search_term = f"{endpoint}/datasetGroupings"
    request = requests.get(search_term,auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200

def test_createDatasetGroupings():
    search_term = f"{endpoint}/datasetGroupings"
    payload = {
        "name": "pytest",
        "datasets" : [
            {"datasetCategory" : "midb", "datasetId" : "mars-mock"},
            {"datasetCategory" : "enhanced-intelligence", "datasetId" : "sigint"}
        ],
        "description": "pytest"
    }
    request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200

def test_modifyDatasetGroupings():
    search_term = f"{endpoint}/datasetGroupings"
    payload = {
        "name": "pytest",
        "datasets" : [
            {"datasetCategory" : "midb", "datasetId" : "mars-mock"},
            {"datasetCategory" : "enhanced-intelligence", "datasetId" : "geoint"}
        ],
        "description": "pytest"
    }
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200

def test_deleteDatasetGroupings():
    search_term = f"{endpoint}/datasetGroupings/pytest"
    payload = {
        "name": "pytest",
        "datasets" : [
            {"datasetCategory" : "midb", "datasetId" : "mars-mock"},
            {"datasetCategory" : "enhanced-intelligence", "datasetId" : "geoint"}
        ],
        "description": "pytest"
    }
    request = requests.delete(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 204