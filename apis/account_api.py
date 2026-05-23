import requests


class AccountAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def create_account(self, user_name, initial_balance):

        payload = {
            "user_name": user_name,
            "initial_balance": initial_balance
        }

        response = requests.post(
            f"{self.BASE_URL}/posts",
            json=payload
        )

        return response


    def get_account(self, account_id):

        response = requests.get(
            f"{self.BASE_URL}/posts/{account_id}"
        )

        return response


    def update_account(self, account_id, data):

        response = requests.put(
            f"{self.BASE_URL}/posts/{account_id}",
            json=data
        )

        return response


    def delete_account(self, account_id):

        response = requests.delete(
            f"{self.BASE_URL}/posts/{account_id}"
        )

        return response