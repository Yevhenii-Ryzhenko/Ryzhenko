"""
В заданні вказано: "від 0 до N". Але немає уточнення, чи включно з N, чи ні. Тому зроблено два варіанти
"""

def fibonacci_numbers_including_n(n):

    a, b = 0, 1

    while a<=n:
        yield a
        a, b = b, a + b

def fibonacci_numbers_not_including_n(n):

    a, b = 0, 1

    while a<n:
        yield a
        a, b = b, a + b

for num in fibonacci_numbers_including_n(21):
    print(num)

print('-' * 80)

for num in fibonacci_numbers_not_including_n(21):
    print(num)