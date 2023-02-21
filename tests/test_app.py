"""Integration tests for app.py"""
from typing import Type
from flask.testing import FlaskClient
from flask.wrappers import Response
import pytest

from bank_api.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_account_creation_successful(client: FlaskClient):
    # Use the client to make requests to the Flask app.
    # response = client.get('/example/route')
    # Or use client.post to make a POST request
    # https://flask.palletsprojects.com/en/1.1.x/testing/
    account_name_test = 'Manolo'
    account_path_to_test = '/accounts/' + account_name_test

    response = client.post(account_path_to_test)
    assert(response.status_code == 200)
    response = client.get(account_path_to_test)
    assert(response.json["name"] == account_name_test)

def test_account_creation_duplicated_account(client: FlaskClient):
    account_name_test = 'Pere'
    account_path_to_test = '/accounts/' + account_name_test

    response = client.post(account_path_to_test)
    assert(response.status_code == 200)

    # try to create it again
    response = client.post(account_path_to_test)
    assert(response.status_code == 400)#bad request

def test_account_account_does_not_exist(client: FlaskClient):
    account_name_test = 'Does not exist'
    account_path_to_test = '/accounts/' + account_name_test

    response = client.get(account_path_to_test)
    assert(response.status_code == 404)
    
