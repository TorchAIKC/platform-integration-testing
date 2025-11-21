import json
import pytest
import requests
from requests.auth import HTTPBasicAuth

with open("config/_temp/creds.json") as datafile:
    creds = json.load(datafile)
    endpoint =  creds['endpoint']
    username = creds['username']
    password = creds['password']

def test_adminGetAllDatasetInternal():
    search_term = f"{endpoint}/admin/datasets/internal"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminCreateDatasetInternal():
    payload = {
      "partitionEntities": [
        {
          "id": 0,
          "colName": "string",
          "colType": "string"
        }
      ],
      "temporalDataColName": "string",
      "temporalDataColType": "string",
      "temporalDataColFormat": "string",
      "latColumn": "string",
      "longColumn": "string",
      "sortColumn": "string",
      "sortDirection": "string",
      "id": "pytest",
      "category": "pytest",
      "description": "string",
      "tableName": "string",
      "catalog": "string",
      "schema": "string",
      "enabled": True,
      "datatypeEntities": [
        {
          "id": 0,
          "name": "string",
          "value": "string",
          "type": "string"
        }
      ],
      "internalAllowedRoles": [
        {
          "roleName": "string",
          "id": 0
        }
      ],
      "internalMetadata": [
        {
          "id": 0,
          "columnName": "string",
          "description": "string",
          "logicalTypes": [
            "string"
          ],
          "columns": [
            "string"
          ]
        }
      ],
      "requiredOrFields": [
        "string"
      ],
      "itemLocationField": "string",
      "itemPreciseTimestampField": "string",
      "groupItemField": "string",
      "faMapIcon": "string",
      "downSampledTable": "string",
      "metricsKey": "string"
    }
    search_term = f"{endpoint}/admin/datasets/internal"
    request = requests.post(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminModifyDatasetInternal():
    payload = {
      "partitionEntities": [
        {
          "id": 0,
          "colName": "string",
          "colType": "string"
        }
      ],
      "temporalDataColName": "string",
      "temporalDataColType": "string",
      "temporalDataColFormat": "string",
      "latColumn": "string",
      "longColumn": "string",
      "sortColumn": "string",
      "sortDirection": "string",
      "id": "pytest",
      "category": "pytest",
      "description": "string",
      "tableName": "string",
      "catalog": "string",
      "schema": "string",
      "enabled": True,
      "datatypeEntities": [
        {
          "id": 0,
          "name": "string",
          "value": "string",
          "type": "string"
        }
      ],
      "internalAllowedRoles": [
        {
          "roleName": "string",
          "id": 0
        }
      ],
      "internalMetadata": [
        {
          "id": 0,
          "columnName": "string",
          "description": "string",
          "logicalTypes": [
            "string"
          ],
          "columns": [
            "string"
          ]
        }
      ],
      "requiredOrFields": [
        "string"
      ],
      "itemLocationField": "string",
      "itemPreciseTimestampField": "string",
      "groupItemField": "string",
      "faMapIcon": "string",
      "downSampledTable": "string",
      "metricsKey": "string"
    }
    search_term = f"{endpoint}/admin/datasets/internal"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 201

def test_adminImportDatasetInternal():
    payload = {
      "replace": True,
      "isReplace": False,
      "entities": [
        {
          "partitionEntities": [
            {
              "id": 0,
              "colName": "string",
              "colType": "string"
            }
          ],
          "temporalDataColName": "string",
          "temporalDataColType": "string",
          "temporalDataColFormat": "string",
          "latColumn": "string",
          "longColumn": "string",
          "sortColumn": "string",
          "sortDirection": "string",
          "id": "pytest",
          "category": "pytest",
          "description": "string",
          "tableName": "string",
          "catalog": "string",
          "schema": "string",
          "enabled": True,
          "datatypeEntities": [
            {
              "id": 0,
              "name": "string",
              "value": "string",
              "type": "string"
            }
          ],
          "internalAllowedRoles": [
            {
              "roleName": "string",
              "id": 0
            }
          ],
          "internalMetadata": [
            {
              "id": 0,
              "columnName": "string",
              "description": "string",
              "logicalTypes": [
                "string"
              ],
              "columns": [
                "string"
              ]
            }
          ],
          "requiredOrFields": [
            "string"
          ],
          "itemLocationField": "string",
          "itemPreciseTimestampField": "string",
          "groupItemField": "string",
          "faMapIcon": "string",
          "downSampledTable": "string",
          "metricsKey": "string"
        }
      ]
    }
    search_term = f"{endpoint}/admin/datasets/internal/import"
    request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminGetDatasetInternal():
    datasetId = "pytest"
    search_term = f"{endpoint}/admin/datasets/internal/{datasetId}"
    request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

### Not Working
# def test_adminModifyDatasetInternalDescription():
#     payload = {
#       "description": "pytest",
#       "columnDescriptions": [
#         {
#           "columnName": "string",
#           "description": "string"
#         }
#       ]
#     }
#     datasetId = "pytest"
#     search_term = f"{endpoint}/admin/datasets/internal/{datasetId}/description"
#     request = requests.put(search_term,data=json.dumps(payload),auth=HTTPBasicAuth(username,password))
#     assert request.status_code == 201

def test_adminDisableDatasetInternal():
    datasetId = "pytest"
    search_term = f"{endpoint}/admin/datasets/internal/{datasetId}/disable"
    request = requests.put(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

def test_adminEnableDatasetInternal():
    datasetId = "pytest"
    search_term = f"{endpoint}/admin/datasets/internal/{datasetId}/enable"
    request = requests.put(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 200

### Not Working
# def test_adminGetDatasetInternalSchemaUpdate():
#     datasetId = "pytest"
#     search_term = f"{endpoint}/admin/datasets/internal/{datasetId}/schema/update"
#     request = requests.get(search_term,auth=HTTPBasicAuth(username,password))
#     assert request.status_code == 200
    
def test_adminDeleteDatasetInternal():
    datasetId = "pytest"
    search_term = f"{endpoint}/admin/datasets/internal/{datasetId}"
    request = requests.delete(search_term,auth=HTTPBasicAuth(username,password))
    assert request.status_code == 204