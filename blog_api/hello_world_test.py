import json
import pytest
import requests
from blog_api import app
from flask import request


# create an instance of app & db as a client
@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_hello_world(client):
    BASE = "http://127.0.0.1:5000"

    response = client.get(BASE + "/helloworld")
    print(response)
    custom_header = response.headers.get("Custom-Header")
    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert custom_header == "Hello World Resource"
    assert data["note"] == "hello world"
