import pytest
from apis.fund_transfer_api import FundTransferAPI
from utilities.json_reader import JsonReader


data = JsonReader.read_json("testdata/users.json")


class TestFundTransfer:

    @pytest.mark.parametrize("user_data", data["users"])
    def test_fund_transfer(self, auth_token, user_data):

        api = FundTransferAPI()

        response = api.initiate_transfer(
            sender_id=user_data["sender_id"],
            receiver_id=user_data["receiver_id"],
            amount=user_data["amount"],
            token=auth_token
        )

        assert response.status_code == 201

        response_data = response.json()

        assert response_data["sender_id"] == user_data["sender_id"]
        assert response_data["receiver_id"] == user_data["receiver_id"]
        assert response_data["amount"] == user_data["amount"]