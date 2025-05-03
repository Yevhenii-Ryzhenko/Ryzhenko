print('Введіть текст:')
user_text = input()
count = 0
word_list = set()
for letter in user_text:
    if letter not in word_list:
        word_list.update(letter)

if len(word_list) > 10:
    print(True)
else:
    print(False)