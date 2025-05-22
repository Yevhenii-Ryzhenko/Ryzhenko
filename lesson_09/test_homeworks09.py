import unittest

from homeworks import sea_area, pc_price, even_sum, sum_two_value, arithmetic_mean, reverse_line

class TestPreviousHomework(unittest.TestCase):

    def test_sum_sea_area (self):
        actual_result = sea_area(436402, 37800)
        expected_result = 474202
        self.assertEqual(actual_result, expected_result)

    def test_sum_sea_area_negative (self):
        actual_result = sea_area(436402, 37800)
        expected_result = 0
        self.assertNotEqual(actual_result, expected_result)

    def test_pc_price (self):
        actual_result = pc_price(1179, 18)
        expected_result = 21222
        self.assertEqual(actual_result, expected_result)

    def test_pc_price_negative (self):
        actual_result = pc_price(1179, 18)
        expected_result = 0
        self.assertNotEqual(actual_result, expected_result)


# Далі застосовано правило, що сума парних чисел може бути виключно парним числом.
# Зауважу: у негативному тесті не враховано можливість використання у формулі суми двох непарних чисел, тобто:
# при списку чисел 1,2,3 сума буде парне число (6), і пройде за цим правилом,
# але тести створенні на перевірку парності саме суми.

    def test_even_sum_function (self):
        actual_result = even_sum([1,2,3,4,5,6,7,8,9,10]) % 2
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

    def test_even_sum_function_negative (self):
        actual_result = even_sum([1,2,3,4,5,6,7,8,9,10,11]) % 2
        expected_result = 1
        self.assertNotEqual(actual_result, expected_result)

    def test_sum_two_value_function_v1 (self):
        actual_result = sum_two_value(2,3)
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

# У наступному тесті використано математичне правило суми квадратів двох чисел.

    def test_sum_two_value_function_v2 (self):
        actual_result = (sum_two_value(2,3))**2
        expected_result = ((2**2) + (2*2*3) + (3**2))
        self.assertEqual(actual_result, expected_result)

    def test_sum_two_value_function_negative (self):
        actual_result = sum_two_value(2,3)
        expected_result = 0
        self.assertNotEqual(actual_result, expected_result)

    def test_arithmetic_mean_function (self):
        actual_result = arithmetic_mean(2,3,4,5,6,7,8)
        expected_result = 5
        self.assertEqual(actual_result, expected_result)

    def test_arithmetic_mean_function_negative_v1 (self):
        actual_result = arithmetic_mean(2,3,4,5,6,7,8)
        expected_result = 0
        self.assertNotEqual(actual_result, expected_result)

# Наступну перевірку вирішив додати (при обчисленні середнього арифметичного порожнього списку числу
# буде відбуватися ділення на 0), але не до кінця зрозумів, чи саме так повинен працювати тест.
# Готовий виправити, якщо неправильно зрозумів.

    def test_arithmetic_mean_function_negative_v2 (self):
        with self.assertRaises(ZeroDivisionError):
            result = arithmetic_mean()

    def test_reverse_line_function (self):
        actual_result = reverse_line('Hello world!')
        expected_result = 'Hello world!' [::-1]
        self.assertEqual(actual_result, expected_result)

    def test_reverse_line_function_negative (self):
        actual_result = reverse_line('Hello world!')
        expected_result = 'Hello world!'
        self.assertNotEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()