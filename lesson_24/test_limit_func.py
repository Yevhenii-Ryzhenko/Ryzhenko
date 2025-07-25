import pytest
import requests
from requests.auth import HTTPBasicAuth


@pytest.mark.usefixtures("auth_to_cars_app")
class TestLimit:

    @pytest.fixture(autouse=True)
    def setup_class(self, auth_to_cars_app, test_logger):
        self.token = auth_to_cars_app["access_token"]
        self.logger = test_logger

    @pytest.mark.parametrize("limit", [0, 1, 10, 25])
    def test_limit(self, limit):
        self.logger.info(f"Test with limit {limit}")
        cars_list = requests.get(url='http://127.0.0.1:8080/cars?sort_by,limit',
                                 params={'limit': limit},
                                 headers={'Authorization': f'Bearer {self.token}'}).json()
        assert len(cars_list) == limit

    @pytest.mark.parametrize("limit", [-1, 26])
    def test_limit_negative(self, limit):
        self.logger.info(f"Negative test with limit {limit}")
        cars_list = requests.get(url='http://127.0.0.1:8080/cars?sort_by,limit',
                                 params={'limit': limit},
                                 headers={'Authorization': f'Bearer {self.token}'}).json()
        assert len(cars_list) != limit
