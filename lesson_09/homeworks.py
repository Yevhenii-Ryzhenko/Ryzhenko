"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
def sea_area (black_sea_area: int, azov_sea_area: int):
    return black_sea_area + azov_sea_area
sea_area(436402, 37800)

"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

def pc_price(part_price: int|float, date: int):
    full_price = part_price * date
    return full_price

pc_price(1179, 18)

"""
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті.
"""

def even_sum(list: list):
    sum_1 = 0
    for value in list:
        if value % 2 == 0:
            sum_1 += value
    return sum_1

"""
Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_value (value_1, value_2):
    return value_1 + value_2

"""
Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean (*args):
    return sum(args) / len(args)

"""
Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_line (user_text):
    return user_text [::-1]


