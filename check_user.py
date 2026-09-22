import sqlite3

from database_init import DATABASE_NAME


def check_user(username, password):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name
        FROM users
        WHERE username = ?
        AND password = ?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user
