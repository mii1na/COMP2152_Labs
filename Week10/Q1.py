# ============================================================
#  WEEK 10 LAB — Q1: PASSWORD VAULT
#  COMP2152 — Mina Fahim
# ============================================================

import sqlite3


DB_NAME = "vault.db"


# --- Helpers (provided) ---
def setup_database():
    """Create the vault table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS vault (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT,
        username TEXT,
        password TEXT
    )""")
    conn.commit()
    conn.close()


def display_credentials(credentials):
    """Pretty-print a list of credential rows."""
    if not credentials:
        print("  (no results)")
        return
    for row in credentials:
        print(f"  {row[1]:<14} | {row[2]:<12} | {row[3]}")


def add_credential(website, username, password):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO vault (website, username, password) VALUES (?, ?, ?)",
                     (website, username, password))

def get_all_credentials():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT * FROM vault ORDER BY website ASC").fetchall()

def find_credential(website):
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute("SELECT * FROM vault WHERE website = ?", (website,)).fetchall()