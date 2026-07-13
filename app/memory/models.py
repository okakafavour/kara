from app.memory.database import Database


class MemoryModel:

    def __init__(self):
        self.db = Database()

    def save(self, key: str, value: str):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            INSERT INTO memories (key, value)
            VALUES (?, ?)
            ON CONFLICT(key)
            DO UPDATE SET
                value = excluded.value,
                updated_at = CURRENT_TIMESTAMP
            """,
            (key, value),
        )

        self.db.connection.commit()

    def get(self, key: str):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            SELECT value
            FROM memories
            WHERE key = ?
            """,
            (key,),
        )

        row = cursor.fetchone()

        return row["value"] if row else None

    def delete(self, key: str):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            DELETE FROM memories
            WHERE key = ?
            """,
            (key,),
        )

        self.db.connection.commit()

    def get_all(self):

        cursor = self.db.connection.cursor()

        cursor.execute(
            """
            SELECT key, value
            FROM memories
            ORDER BY key
            """
        )

        return cursor.fetchall()