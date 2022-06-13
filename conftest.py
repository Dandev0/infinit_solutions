import pytest
import requests

url = 'XXX'                     #url(API)
body = {
    "company_name": "Тестовая компания",
    "company_type": "ООО",
    "company_users": ["test_cu_11@mail.com", "test_dev@mail.com",
                      "ivan@noibiz.com"],
    "email_owner": "aa+1@mail.com",
}


@pytest.fixture                 #making a request
def start_request():
    request = requests.post(url, json=body)
    response = request
    return response


@pytest.fixture                  #we get the answer and convert the object to a string
def reformat(start_request):
    response_json = start_request.json()
    return response_json



