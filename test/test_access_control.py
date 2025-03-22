# test/test_access_control.py

def test_dashboard_requires_login(client):
    response = client.get('/', follow_redirects=True)
    assert b'Login' in response.data
    assert b'Username' in response.data 

def test_start_quiz_requires_login(client):
    response = client.get('/start_quiz/easy', follow_redirects=True)
    assert b'Login' in response.data
    assert b'Username' in response.data

def test_question_requires_login(client):
    response = client.get('/quiz/question/easy', follow_redirects=True)
    assert b'Login' in response.data

def test_result_requires_login(client):
    response = client.get('/quiz/result/easy', follow_redirects=True)
    assert b'Login' in response.data
