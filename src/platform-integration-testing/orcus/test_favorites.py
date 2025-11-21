import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("orcus_creds.json") as datafile:
    creds = json.load(datafile)
    endpoint = creds['endpoint']
    my_username = creds['username']
    my_password = creds['password']

def test_getFavoriteDatasets():
    search_term = f"{endpoint}/favorite/datasets"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200
    
def test_createFavoriteDatasets():
    search_term = f"{endpoint}/favorite/datasets"
    payload = {"datasetCategory" : "midb", "datasetId" : "mars-mock"}
    request = requests.post(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 201
    
def test_deleteFavoriteDatasets():
    search_term = f"{endpoint}/favorite/datasets"
    payload = {"datasetCategory" : "midb", "datasetId" : "mars-mock"}
    request = requests.delete(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 204

def test_getFavoriteQueries():
    search_term = f"{endpoint}/favorite/queries"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200

def test_createFavoriteQueries():
    search_term = f"{endpoint}/favorite/queries"
    payload = {
        "queryName": "pytest",
        "datasetCategory" : "midb", 
        "datasetId" : "mars-mock", 
        "query": {
            "timeRange":{
                "start":"2025-07-01T00:00:00.000Z","end":"2025-07-31T00:00:00.000Z"
            },
            "geospatial":{
                "polygons":"(111.88476562500001 12.708937672385346, 111.88476562500001 21.1091002243719, 120.23437500000001 21.1091002243719, 120.23437500000001 12.708937672385346, 111.88476562500001 12.708937672385346)",
                "antimeridianPolygons": False
            },
            "filters":[{"name":"classification_color","value":"GREEN","operator":"="}]
        }
    }
    request = requests.post(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 201

def test_deleteFavoriteQueries():
    search_term = f"{endpoint}/favorite/queries"
    payload = {"queryName": "pytest","datasetCategory" : "midb", "datasetId" : "mars-mock"}
    request = requests.delete(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 204

def test_getFavoriteGraphs():
    search_term = f"{endpoint}/favorite/graphTemplates"
    request = requests.get(search_term, auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 200

def test_createFavoriteGraphs():
    search_term = f"{endpoint}/favorite/graphTemplates"
    payload = {
      "datasetCategory": "midb",
      "datasetId": "mars-mock",
      "templateName": "string",
      "templateJson": "string"
    }
    request = requests.post(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 201


def test_deleteFavoriteGraphs():
    search_term = f"{endpoint}/favorite/graphTemplates"
    payload = {
      "datasetCategory": "midb",
      "datasetId": "mars-mock",
      "templateName": "string",
      "templateJson": "string"
    }
    request = requests.delete(search_term, data=json.dumps(payload), auth=HTTPBasicAuth(my_username,my_password))
    assert request.status_code == 204