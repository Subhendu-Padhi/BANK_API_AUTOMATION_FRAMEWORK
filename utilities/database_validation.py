# utilities/database_validation.py

import pymysql

class DBValidation:

    def verify_transaction(transaction_id):

        connection=pymysql.connect(

            host="localhost",
            user="root",
            password="root",
            database="bank"

        )

        cursor=connection.cursor()

        query=f"""

        select amount
        from transaction_table
        where transaction_id={transaction_id}

        """

        cursor.execute(query)

        return cursor.fetchone()