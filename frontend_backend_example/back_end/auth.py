import sqlite3
from pathlib import Path

# Correct path to your database
db_path = Path(__file__).parent / "database" / "database.db"

def user_sign_up(name, surname, email, password):
    print(f"name: {name}, surname: {surname}, email: {email}, password: {password}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Ensure the table exists (optional but safe)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    ''')

    try:
        # Insert the user data
        cursor.execute('''
            INSERT INTO users (name, surname, email, password)
            VALUES (?, ?, ?, ?)
        ''', (name, surname, email, password))
        conn.commit()
        print("✅ User registered successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ Email already exists!")
    finally:
        conn.close()
