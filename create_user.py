import sqlite3

from database_init import DATABASE_NAME


def create_user(name, username, password):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users
            (name, username, password)
            VALUES (?, ?, ?)
            """,
            (name, username, password)
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()
