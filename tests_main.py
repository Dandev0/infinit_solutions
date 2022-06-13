"""TESTS"""
from conftest import body          #we get the body of the transmitted data in request


def test_check_status_code(start_request):
    assert start_request.status_code == 200


def test_http_api(reformat):               #checking the status of the request
    assert reformat["type"] == "success"


def test_name_response(reformat):          #checking the equality of the transmitted name
    try:
        assert reformat['company']['name'] == body["company_name"]
    except:
        raise AssertionError('Не сходится имя')


def test_check_useers(reformat):            #check the correspondence of the sent and received users
    assert reformat["company"]['type'] == body["company_type"]
    assert reformat["company"]["users"] == body["company_users"]
