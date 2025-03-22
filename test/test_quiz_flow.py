# test/test_quiz_flow.py

def register_and_login(client):
    client.post('/register', data={
        'username': 'quizuser',
        'password': 'testpass'
    }, follow_redirects=True)

    client.post('/login', data={
        'username': 'quizuser',
        'password': 'testpass'
    }, follow_redirects=True)

def test_quiz_start_and_question_display(client):
    register_and_login(client)

    response = client.get('/start_quiz/easy', follow_redirects=True)
    assert b'Question' in response.data or b'select the correct answer' in response.data
    assert b'Option A' in response.data

def test_quiz_submit_and_result(client):
    register_and_login(client)

    client.get('/start_quiz/easy', follow_redirects=True)

    # Simulate one question answer
    response = client.post('/quiz/question/easy', data={'answer': 'A'}, follow_redirects=True)
    assert b'Explanation' in response.data or b'Next' in response.data

    # Simulate finishing the quiz (skip to end)
    for _ in range(9):
        client.post('/quiz/question/easy', data={'answer': 'A'}, follow_redirects=True)

    result_response = client.get('/quiz/result/easy', follow_redirects=True)
    assert b'Your Score' in result_response.data or b'out of 10' in result_response.data
