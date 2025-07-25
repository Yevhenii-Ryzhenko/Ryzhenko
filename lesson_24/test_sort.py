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
    def test_sorted_func_for_category(self, sort_category):
        self.logger.info(f"Test with sorted by {sort_category}")
        cars_list = requests.get(url=f'http://127.0.0.1:8080/cars?sort_by,limit',
                                 params={'sort_by': sort_category, "order": "desc"},
                                 headers={'Authorization': f'Bearer {self.token}'}).json()
        k_zero = 0
        max_value = [car[f'{sort_category}'] for car in cars_list]
        for k in cars_list:
            if k[f'{sort_category}'] >= k_zero:
                k_zero = k[f'{sort_category}']
            else:
                raise AssertionError
        assert k_zero == max(max_value)

    @pytest.mark.parametrize("order", ["desc", "asc"])
    def test_sorted_func_for_asc_and_desc(self, order):
        self.logger.info(f"Test with sorted by {order}")
        cars_list = requests.get(url=f'http://127.0.0.1:8080/cars?sort_by,limit',
                                 params={'sort_by': "year", "order": order},
                                 headers={'Authorization': f'Bearer {self.token}'}).json()
        k_zero = 2100
        min_value = [car["year"] for car in cars_list]
        for k in cars_list:
            if k["year"] <= k_zero:
                k_zero = k["year"]
        assert k_zero == min(min_value)

    @pytest.mark.parametrize("order", ["desc"])
    def test_sorted_name(self, order):
        self.logger.info(f"Test with sorted name by {order}")
        cars_list = requests.get(
            url='http://127.0.0.1:8080/cars?sort_by,order',
            params={'sort_by': "brand", 'order': order},
            headers={'Authorization': f'Bearer {self.token}'}
        ).json()

        values = [car["brand"] for car in cars_list]

        sorted_values = sorted(values)

        assert values == sorted_values