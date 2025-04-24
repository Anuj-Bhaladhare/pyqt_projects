from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import sqlite3

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










from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()
db_path = "users.db"  # Set your DB path

# Pydantic model to validate request body
class User(BaseModel):
    name: str
    surname: str
    email: str
    password: str

# Create the users table if not exists
def create_user_table():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_user_table()

@app.post("/signup")
def user_sign_up(user: User):
    print(f"Received: {user}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO users (name, surname, email, password)
            VALUES (?, ?, ?, ?)
        ''', (user.name, user.surname, user.email, user.password))
        conn.commit()
        return {"message": "✅ User registered successfully!"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="⚠️ Email already exists!")
    finally:
        conn.close()
