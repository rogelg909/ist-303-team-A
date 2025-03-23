import sqlite3
import os

def init_db(db_path='database.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fix: Get absolute path to schema.sql
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')

    with open(schema_path, 'r') as f:
        cursor.executescript(f.read())

    # ✅ Insert sample questions if none exist
    cursor.execute("SELECT COUNT(*) FROM quiz_questions")
    count = cursor.fetchone()[0]

    if count == 0:
        print("Inserting sample questions...")

        sample_questions = [
            ("easy", "What is the capital of France?", "Paris", "London", "Berlin", "Madrid", "A", "Paris is the capital of France."),
            ("easy", "What is 2 + 2?", "3", "4", "5", "2", "B", "2 + 2 equals 4."),
            ("medium", "Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", "C", "Mars is known as the Red Planet."),
            ("hard", "Who developed the theory of relativity?", "Newton", "Einstein", "Tesla", "Hawking", "B", "Einstein developed the theory of relativity.")
        ]

        for q in sample_questions:
            cursor.execute("""
                INSERT INTO quiz_questions (category, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, q)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
