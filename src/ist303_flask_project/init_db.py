import sqlite3
import os

def init_db(db_path='database.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Fix: Get absolute path to schema.sql
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')

    with open(schema_path, 'r') as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()



