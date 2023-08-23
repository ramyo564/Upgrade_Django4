import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import (
       AccountFactory,
       UserProfileFactory,
)
register(AccountFactory)
register(UserProfileFactory)


@pytest.fixture
def api_client():
    return APIClient
