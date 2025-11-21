import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("orcus_creds.json") as datafile:
    creds = json.load(datafile)
    endpoint = creds['endpoint']
    my_username = creds['username']
    my_password = creds['password']
    
def getApiKey():
    search_term = f"{endpoint}/apiKeys"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    for each in request.json():
        if each['name'] == "pytest":
            return each['key']
    
def test_createAPIKeys():
    search_term = f"{endpoint}/apiKeys"
    payload = {
        "name": "pytest",
        "datasets": [{"datasetCategory" : "midb", "datasetId" : "mars-mock"}],
        "filesetIds": ["midb"],
        "ecosystemNames": []
    }
    request = requests.post(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200

def test_modifyAPIKeys():
    search_term = f"{endpoint}/apiKeys"
    payload = {
        "name": "pytest",
        "datasets": [
            {"datasetCategory" : "midb", "datasetId" : "mars-mock"},
            {"datasetCategory" : "enhanced-intelligence", "datasetId" : "sigint"},
            ],
        "filesetIds": [
            "midb",
            "enhanced-intelligence"
            ],
            "ecosystemNames": []
    }
    request = requests.put(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    
def test_getAPIKeys():
    search_term = f"{endpoint}/apiKeys"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200

def test_listDatasets():
    search_term = f"{endpoint}/datasets"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.get(search_term, headers=api_key_header)
    assert request_key.status_code == 200
    
def test_describeDataset():
    category = "midb"
    datasetID = "mars-mock"
    search_term = f"{endpoint}/datasets/{category}/{datasetID}/describe"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.get(search_term, headers=api_key_header)
    assert request_key.status_code == 200

def test_sampleDataset():
    category = "midb"
    datasetID = "mars-mock"
    search_term = f"{endpoint}/datasets/{category}/{datasetID}/sample"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.get(search_term, headers=api_key_header)
    assert request_key.status_code == 200

def test_filterDataset():
    payload = {
        "paging":{
            "offset":0,
            "max":25
        },
        "timeRange":{
            "start":"2025-07-01T00:00:00.000Z","end":"2025-07-31T00:00:00.000Z"
        },
        "geospatial":{
            "polygons":"(111.88476562500001 12.708937672385346, 111.88476562500001 21.1091002243719, 120.23437500000001 21.1091002243719, 120.23437500000001 12.708937672385346, 111.88476562500001 12.708937672385346)",
            "antimeridianPolygons": False
        },
        "filters":[{"name":"classification_color","value":"GREEN","operator":"="}],
        "columns": ["entry_id"]
    }
    category = "enhanced-intelligence"
    datasetID = "sigint"
    search_term = f"{endpoint}/datasets/{category}/{datasetID}/search"
    request = requests.post(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.post(search_term, data=json.dumps(payload), headers=api_key_header)
    assert request_key.status_code == 200

def test_streamDataset():
    payload = {
        "paging":{
            "offset":0,
            "max":25
        },
        "timeRange":{
            "start":"2025-07-01T00:00:00.000Z","end":"2025-07-31T00:00:00.000Z"
        },
        "geospatial":{
            "polygons":"(111.88476562500001 12.708937672385346, 111.88476562500001 21.1091002243719, 120.23437500000001 21.1091002243719, 120.23437500000001 12.708937672385346, 111.88476562500001 12.708937672385346)",
            "antimeridianPolygons": False
        },
        "filters":[{"name":"classification_color","value":"GREEN","operator":"="}],
        "columns": ["entry_id"]
    }
    category = "enhanced-intelligence"
    datasetID = "sigint"
    search_term = f"{endpoint}/datasets/{category}/{datasetID}/stream"
    request = requests.post(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.post(search_term, data=json.dumps(payload), headers=api_key_header)
    assert request_key.status_code == 200

def test_aggData():
    payload = {
        "timeRange":{
            "start":"2025-07-01T00:00:00.000Z","end":"2025-07-31T00:00:00.000Z"
        },
        "geospatial":{
            "polygons":"(111.88476562500001 12.708937672385346, 111.88476562500001 21.1091002243719, 120.23437500000001 21.1091002243719, 120.23437500000001 12.708937672385346, 111.88476562500001 12.708937672385346)",
            "antimeridianPolygons": False
        },
        "filters":[{"name":"classification_color","value":"GREEN","operator":"="}]
    }
    category = "enhanced-intelligence"
    datasetID = "sigint"
    aggregationType = "count" 
    columnName = "entry_id"
    search_term = f"{endpoint}/datasets/{category}/{datasetID}/aggregate/{aggregationType}/{columnName}"
    request = requests.post(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.post(search_term, data=json.dumps(payload), headers=api_key_header)
    assert request_key.status_code == 200

def test_listFilesets():
    search_term = f"{endpoint}/filesets"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.get(search_term, headers=api_key_header)
    assert request_key.status_code == 200

def test_listNestedFile():
    filesetID = "midb"
    search_term = f"{endpoint}/filesets/{filesetID}/list"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.get(search_term, headers=api_key_header)
    assert request_key.status_code == 200

def test_getFileTags():
    filesetID = "midb"
    filename = "mars-mock/2025-08-06.csv"
    search_term = f"{endpoint}/filesets/{filesetID}/tags?file={filename}"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password)) 
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.get(search_term, headers=api_key_header)
    assert request_key.status_code == 200
    
def test_downloadFile():
    filesetID = "midb"
    filename = "mars-mock/2025-08-06.csv"
    search_term = f"{endpoint}/filesets/{filesetID}/download?file={filename}"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    api_key_header = {'x-api-key': getApiKey()}
    request_key = requests.get(search_term, headers=api_key_header)
    assert request_key.status_code == 200

### Need test fileset to upload
# def test_uploadFileURL():
#     filesetID = "pytest"
#     filename = "pytest.txt"
#     search_term = f"{endpoint}/filesets/{filesetID}/upload?file={filename}"
#     request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
#     assert request.status_code == 200
#     api_key_header = {'x-api-key': getApiKey()}
#     request_key = requests.get(search_term, headers=api_key_header)
#     assert request_key.status_code == 200

def test_deleteAPIKeys():
    search_term = f"{endpoint}/apiKeys/pytest"
    request = requests.delete(search_term, auth=HTTPBasicAuth(my_username,my_password))
    search_term_get = f"{endpoint}/apiKeys/"
    request_get = requests.get(search_term_get, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 204
    assert len(request_get.json()) == 0