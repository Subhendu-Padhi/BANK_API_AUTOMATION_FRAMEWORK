import requests


class FundTransferAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def initiate_transfer(self, sender_id, receiver_id, amount, token):

        url = f"{self.BASE_URL}/posts"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        payload = {
            "sender_id": sender_id,
            "receiver_id": receiver_id,
            "amount": amount
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        return response