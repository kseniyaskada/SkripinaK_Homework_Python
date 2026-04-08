import requests
import pytest

base_url = "https://ru.yougile.com/api-v2"
my_token = ""  # здесь должен быть токен
id = ""  # здесь должно быть id компании


@pytest.mark.positive_test
def test_create_project():
    body = {
        'title': 'Lesson8'
    }
    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_token}"
    }
    resp = requests.post(base_url+"/projects", json=body, headers=my_headers)
    response_data = resp.json()

    assert resp.status_code == 201
    assert 'id' in response_data


@pytest.mark.negative_test
def test_create_project_no_title():
    body = {
        'title': ''
    }
    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_token}"
    }
    resp = requests.post(base_url+"/projects", json=body, headers=my_headers)

    assert resp.status_code == 400


@pytest.mark.positive_test
def test_get_by_id():

    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_token}"
    }

    resp = requests.get(
        base_url+"/projects/"+id,
        headers=my_headers)

    assert resp.status_code == 200


@pytest.mark.negative_test
def test_get_by_uncorrect_id():
    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_token}"
    }

    resp = requests.get(
        base_url+"/projects/qwerty12345",
        headers=my_headers)

    assert resp.status_code == 404


@pytest.mark.positive_test
def test_change_project():

    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_token}"
    }

    body = {
        "title": "lesson8 Update"
    }

    resp = requests.put(
        base_url+"/projects/"+id,
        json=body,
        headers=my_headers)

    assert resp.status_code == 200


@pytest.mark.negative_test
def test_change_project_empty_title():

    my_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_token}"
    }

    body = {
        "title": ""
    }

    resp = requests.put(
        base_url+"/projects/28b31a10-6431-4f10-bd39-89fadd884103",
        headers=my_headers,
        json=body
    )

    assert resp.status_code == 400
