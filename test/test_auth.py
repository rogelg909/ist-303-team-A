# test/test_auth.py

def test_register_login_logout_flow(client):
    # Register a new user
    response = client.post('/register', data={
        'username': 'authuser',
        'password': 'secret123'
    }, follow_redirects=True)
    assert b'Registration successful' in response.data

    # Login with correct credentials
    response = client.post('/login', data={
        'username': 'authuser',
        'password': 'secret123'
    }, follow_redirects=True)
    assert b'Hello' in response.data
    assert b'Logout' in response.data

    # Logout
    response = client.get('/logout', follow_redirects=True)
    assert b'You have been logged out.' in response.data
    assert b'Login' in response.data


def test_login_with_wrong_password(client):
    # Register user first
    client.post('/register', data={
        'username': 'wrongpassuser',
        'password': 'mypassword'
    }, follow_redirects=True)

    # Try wrong login
    response = client.post('/login', data={
        'username': 'wrongpassuser',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    assert b'Invalid credentials' in response.data

