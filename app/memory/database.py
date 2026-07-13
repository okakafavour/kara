import sqlite3
from pathlib import Path


class Database:
    """Handles the SQLite database connection."""

    def __init__(self):
        self.db_path = Path(__file__).parent / "memory.db"

        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row

        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()