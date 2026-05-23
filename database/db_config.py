import sqlite3
import os


class DBConnection:

    DB_PATH = os.path.join(os.path.dirname(__file__), "bank.db")

    @staticmethod
    def get_connection():

        conn = sqlite3.connect(DBConnection.DB_PATH)
        return conn