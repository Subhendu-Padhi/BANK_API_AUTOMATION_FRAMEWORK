# apis/transaction_api.py

import requests


class TransactionAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def transfer_money(
            self,
            sender_id,
            receiver_id,
            amount,
            token
    ):

        headers = {
            "Authorization": f"Bearer {token}"
        }

        payload = {
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "amount": amount
        }

        response = requests.post(
            f"{self.BASE_URL}/posts",
            json=payload,
            headers=headers
        )

        return response