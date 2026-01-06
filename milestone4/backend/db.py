import sqlite3

conn = sqlite3.connect("history.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT
)
""")
conn.commit()

def save_topic(topic):
    cursor.execute("INSERT INTO history (topic) VALUES (?)", (topic,))
    conn.commit()

def get_history():
    cursor.execute("SELECT topic FROM history")
    return [row[0] for row in cursor.fetchall()]
