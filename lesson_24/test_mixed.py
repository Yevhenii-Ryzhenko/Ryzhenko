import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.mark.usefixtures("auth_to_cars_app")
class TestSorted:

    @pytest.fixture(autouse=True)
    def setup_class(self, auth_to_cars_app, test_logger):
        self.token = auth_to_cars_app["access_token"]
        self.logger = test_logger

    @pytest.mark.parametrize("sort_category", ["year", "engine_volume", "price"])
    @pytest.mark.parametrize("limit", [1, 10, 25])
    def test_limit(self, sort_category, limit):
        self.logger.info(f"Test with limit {limit} and sorted by {sort_category}")
        cars_list = requests.get(url='http://127.0.0.1:8080/cars?sort_by,limit',
                                 params={'limit': limit, "sort_by": sort_category},
                                 headers={'Authorization': f'Bearer {self.token}'}).json()
        k_zero = 0
        max_value = [car[f'{sort_category}'] for car in cars_list]
        for k in cars_list:
            if k[f'{sort_category}'] >= k_zero:
                k_zero = k[f'{sort_category}']
            else:
                raise AssertionError

        assert k_zero == max(max_value)
        assert len(cars_list) == limit
