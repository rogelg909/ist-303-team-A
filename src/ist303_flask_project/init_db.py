import sqlite3
import os

def column_exists(cursor, table, column):
    cursor.execute(f"PRAGMA table_info({table})")
    return any(col[1] == column for col in cursor.fetchall())

def init_db(db_path='database.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r') as f:
        cursor.executescript(f.read())

    # Add 'topic' column if it doesn't exist
    if not column_exists(cursor, "quiz_questions", "topic"):
        cursor.execute("ALTER TABLE quiz_questions ADD COLUMN topic TEXT")
        print("✅ Added 'topic' column to quiz_questions table.")

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
    print("✅ Database initialized successfully!")

if __name__ == "__main__":
    init_db()

