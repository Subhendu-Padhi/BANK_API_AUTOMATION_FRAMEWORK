from database.db_config import DBConnection


class DBSetup:

    @staticmethod
    def create_tables():

        conn = DBConnection.get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            balance INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER,
            receiver_id INTEGER,
            amount INTEGER
        )
        """)

        conn.commit()
        conn.close()