# apis/auth_api.py

import requests


class AuthAPI:

    BASE_URL = "https://reqres.in/api"

    def generate_token(self):

        payload = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        response = requests.post(
            f"{self.BASE_URL}/login",
            json=payload
        )

        return response