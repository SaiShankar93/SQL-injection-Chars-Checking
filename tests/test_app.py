import requests

def test_index_route():
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200 

def test_empty_input():
    response = requests.post('http://localhost:5000/v1/sanitized/input/', data={'text': ''})
    res = response.json()
    assert res['result'] == 'empty'
    assert response.status_code == 200

def test_sanitized_input():
    response = requests.post('http://localhost:5000/v1/sanitized/input/', data={'text': 'testing_sanitized_input'})
    res = response.json()
    assert res['result'] == 'sanitized'
    assert response.status_code == 200

def test_unsanitized_input():
    response = requests.post('http://localhost:5000/v1/sanitized/input/', data={'text': '--?>,*ksks'})
    res = response.json()
    assert res['result'] == 'unsanitized'
    assert response.status_code == 200