# conftest.py

import pytest
from utilities.token_manager import TokenManager


@pytest.fixture(scope="session")
def auth_token():

    token = TokenManager.get_token()

    return token