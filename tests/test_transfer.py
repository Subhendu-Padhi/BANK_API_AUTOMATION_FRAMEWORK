import pytest
from apis.transaction_api import TransactionAPI
from utilities.json_reader import JsonReader


data = JsonReader.read_json("testdata/users.json")


class TestMoneyTransfer:

    @pytest.mark.parametrize("user_data", data["users"])
    def test_transfer_amount(self, auth_token, user_data):

        transfer = TransactionAPI()

        response = transfer.transfer_money(
            sender_id=user_data["sender_id"],
            receiver_id=user_data["receiver_id"],
            amount=user_data["amount"],
            token=auth_token
        )

        assert response.status_code == 201