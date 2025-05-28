import pytest
from lesson_12.biometric import access_level

"""
database_users = [
  {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
  {"id": 2, "name": "Jane", "second_name": "Joi", "age": 26},
]
"""

@pytest.mark.parametrize("actual, expected", [
  ({"id": 1, "name": "John", "second_name": "Doe", "age": 30}, "full"),
  ({"id": 2, "name": "Jane", "second_name": "Joi", "age": 26}, "full"),
  ({"id": 1, "name": "John", "second_name": "Joi", "age": 30}, "read-only"),
  ({"id": 1, "name": "Jane", "second_name": "Doe", "age": 30}, "read-only"),
  ({"id": 1, "name": "John", "second_name": "Doe", "age": 26}, "read-only"),
  ({"id": 2, "name": "John", "second_name": "Joi", "age": 26}, "read-only"),
  ({"id": 2, "name": "Jane", "second_name": "Doe", "age": 26}, "read-only"),
  ({"id": 2, "name": "Jane", "second_name": "Joi", "age": 30}, "read-only"),
  ({"id": 1, "name": "Jane", "second_name": "Joi", "age": 30}, "forbiden"),
  ({"id": 1, "name": "John", "second_name": "Joi", "age": 26}, "forbiden"),
  ({"id": 2, "name": "John", "second_name": "Doe", "age": 30}, "forbiden"),
  ({"id": 3, "name": "John", "second_name": "Doe", "age": 30}, "forbiden"),
  ({"id": 4, "name": "Jane", "second_name": "Joi", "age": 26}, "forbiden"),
  ({"name": "Jane", "second_name": "Joi", "age": 26}, "User is not found"),
  ({"id": 1, "second_name": "Doe", "age": 30}, "You provided insufficient data"),
  ({"id": 1, "name": "John", "age": 30}, "You provided insufficient data"),
  ({"id": 1, "name": "John", "second_name": "Doe"}, "You provided insufficient data"),
])


def test_biometric(actual, expected):
  assert access_level(actual) == expected