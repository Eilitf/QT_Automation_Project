import pytest
import requests as requests

@pytest.fixture(scope='module')
def req():
    with requests.Session() as s:
        s.headers.update({
            'Accept': 'application/json'
        })
        yield s


"""
    get pet by id 7574746.  if pet exist-> expecting true
"""


def test_get_pet_by_id(req):
    response = requests.get('https://petstore.swagger.io/v2/pet/7574746')
    response_body = response.json()
    assert response_body['id'] == 7574746


def test_get_user_by_user_name(req):
    response = requests.get('https://petstore.swagger.io/v2/user/user1')
    response_body = response.json()
    assert response_body['message'] == 'User not found'