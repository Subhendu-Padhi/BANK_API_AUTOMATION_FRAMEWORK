from apis.account_api import AccountAPI


class TestAccountAPI:

    def test_create_account(self):

        api = AccountAPI()

        response = api.create_account(
            user_name="John Doe",
            initial_balance=10000
        )

        assert response.status_code == 201

        data = response.json()

        assert data["user_name"] == "John Doe"
        assert data["initial_balance"] == 10000


    def test_get_account(self):

        api = AccountAPI()

        response = api.get_account(1)

        assert response.status_code == 200


    def test_update_account(self):

        api = AccountAPI()

        payload = {
            "user_name": "John Updated",
            "initial_balance": 15000
        }

        response = api.update_account(1, payload)

        assert response.status_code == 200


    def test_delete_account(self):

        api = AccountAPI()

        response = api.delete_account(1)

        assert response.status_code == 200