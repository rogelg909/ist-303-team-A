# test/conftest.py
import pytest
import sys
import os
import tempfile

# Add the application path to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'ist303_flask_project')))

from app import app, get_db_connection
from init_db import init_db

@pytest.fixture
def client():
    # Create a temporary test database
    db_fd, test_db_path = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['DATABASE'] = test_db_path

    with app.test_client() as client:
        with app.app_context():
            # Initialize the database schema
            init_db(test_db_path)

            # Insert a sample quiz question
            conn = get_db_connection()
            conn.execute("""
                INSERT INTO quiz_questions
                (category, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                "easy",
                "What is the capital of France?",
                "Paris", "London", "Berlin", "Madrid",
                "A",
                "Paris is the capital of France."
            ))
            conn.commit()
            conn.close()

        yield client

    # Cleanup
    os.close(db_fd)
    os.unlink(test_db_path)
