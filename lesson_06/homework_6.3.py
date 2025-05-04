lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for value in lst1:
    if isinstance(value, str):
        lst2.append(value)

print(lst2)