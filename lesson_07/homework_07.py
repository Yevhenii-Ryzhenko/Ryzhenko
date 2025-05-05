# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
from itertools import count


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier * number <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        # if  result > 25:
        #     # Enter the action to take if the result is greater than 25
        #     pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
number_1 = 2
number_2 = 3

def sum_two_value (value_1, value_2):
    return value_1 + value_2

result_2 = sum_two_value (number_1, number_2)
print(result_2)


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean (*args):
    return sum(args) / len(args)

print(arithmetic_mean(1,2,3,4,5))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
your_text = 'Написати функцію, яка приймає рядок та повертає його у зворотному порядку.'

def line (user_text):
    return user_text [::-1]

print(line(your_text))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
random_text = 'Написати функцію, яка приймає список слів та повертає найдовше слово у списку.'

def max_word(user_text):
    words = user_text.split()
    max_len = max(len(word) for word in words)
    longest = []
    for word in words:
        if len(word) == max_len:
            longest.append(word)
    return longest

print(max_word(random_text))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 (homework_3 task 4)
"""  Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

def sea_area (black_sea_area = int, azov_sea_area = int):
    return black_sea_area + azov_sea_area

print(f'Загальна площа Чорного та Азовського морів, які омивають терени вільної, незалежної та суверенної України '
      f'становить {sea_area(436402, 37800)} км2')

# task 8 (homework_3 task 5)
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
def storage (storage_all = int, storages_1_and_2 = int, storage_2_and_3 = int):
    storage_1 = storage_all - 222950
    storage_3 = storage_all - 250449
    storage_2 = storage_all - storage_1 - storage_3
    print(f'На першому складі знаходиться {storage_1} товар')
    print(f'На другому складі знаходиться {storage_2} товар')
    print(f'На третьому складі знаходиться {storage_3} товар')
    return

storage(375291, 250449, 222950)

# task 9 (homework_3 task 6)
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

def pc_price(part_price = int|float, date = int):
    full_price = part_price * date
    print(f'Вартість ПК за заданими умовами складає {full_price} грн.')
    return

pc_price(1179, 18)

# task 10 (homework_6.4)
"""
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті.
"""

def even_sum(list = list):
    sum_1 = 0
    for value in list:
        if value % 2 == 0:
            sum_1 += value
    return sum_1

print(f'Сума парних чисел у запропонованому лісті становить {even_sum([1,2,3,4,5,6])}.')
