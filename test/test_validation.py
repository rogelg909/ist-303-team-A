# test/test_validation.py

def test_register_with_empty_fields(client):
    # Missing both username and password
    response = client.post('/register', data={
        'username': '',
        'password': ''
    }, follow_redirects=True)
    assert b'Username already exists' not in response.data
    assert b'Registration successful' not in response.data


def test_register_with_duplicate_username(client):
    # First registration
    client.post('/register', data={
        'username': 'duplicateuser',
        'password': 'abc123'
    }, follow_redirects=True)

    # Second registration with same username
    response = client.post('/register', data={
        'username': 'duplicateuser',
        'password': 'differentpass'
    }, follow_redirects=True)

    assert b'Username already exists' in response.data


def test_login_with_empty_fields(client):
    response = client.post('/login', data={
        'username': '',
        'password': ''
    }, follow_redirects=True)
    assert b'Invalid credentials' in response.data
