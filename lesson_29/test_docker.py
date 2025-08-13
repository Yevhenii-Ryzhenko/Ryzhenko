import psycopg2
import pytest

DB_CONFIG = {
    "dbname": "test_db",
    "user": "test_user",
    "password": "test_password",
    "host": "db",
    "port": "5432"
}

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    yield
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("DROP TABLE users")
    conn.commit()
    cur.close()
    conn.close()

def test_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    assert conn is not None
    conn.close()

def test_insertion():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES ('John') RETURNING id")
    inserted_id = cur.fetchone()[0]
    conn.commit()

    cur.execute("SELECT name FROM users WHERE id=%s", (inserted_id,))
    result = cur.fetchone()
    assert result[0] == "John"

    cur.close()
    conn.close()

def test_update():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("UPDATE users SET name='Mike' WHERE name='John'")
    conn.commit()

    cur.execute("SELECT name FROM users WHERE name='Mike'")
    result = cur.fetchone()
    assert result[0] == "Mike"

    cur.close()
    conn.close()

def test_delete():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name='Mike'")
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
    assert count == 0

    cur.close()
    conn.close()