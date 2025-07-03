"""
В заданні вказано: "від 0 до N". Але немає уточнення, чи включно з N, чи ні. Тому зроблено два варіанти
"""

def even_numbers_including_n(n):

    for r in range(0, n+1):
        if r%2 == 0:
            yield r

def even_numbers_not_including_n(n):

    for r in range(0, n):
        if r%2 == 0:
            yield r


for num in even_numbers_including_n(20):
    print(num)

print('-'*80)

for num in even_numbers_not_including_n(20):
    print(num)