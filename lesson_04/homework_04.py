from itertools import count

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

    #print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

    #print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer_without_spaces = adwentures_of_tom_sawer.strip()
    #print(adwentures_of_tom_sawer_without_spaces)
list_of_adwentures_of_tom_sawer = adwentures_of_tom_sawer_without_spaces.split()
    #print(list_of_adwentures_of_tom_sawer)
adwentures_of_tom_sawer = ' '.join(list_of_adwentures_of_tom_sawer)

    #print(adwentures_of_tom_sawer)
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('Літера "h" зустрічаєьться у тексті', adwentures_of_tom_sawer.count('h'), 'разів. '
      'Також у тексті', adwentures_of_tom_sawer.count('H'), 'разів зустрічається велика літера "H". Тому в загальному '
      'підрахунку данна літера по тексту без врахування регістру зустрічається'
      , adwentures_of_tom_sawer.count('h') + adwentures_of_tom_sawer.count('H'), 'разів.')
    #print (adwentures_of_tom_sawer)
print()
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

result = 0
for word in adwentures_of_tom_sawer.split():
    if word.istitle():
        result += 1
print("У даному тексті слова з великої літери зустрічаються", result, "разів.")
print()

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
find_word = "Tom"
first_index = adwentures_of_tom_sawer.find(find_word)
if first_index == -1:
    print(f'Слово "{find_word}" не зустрічається по тексту. Перевірте слово, регістр і розділові знаки '
          f'та повторіть спробу')
else:
    search_second_tom = adwentures_of_tom_sawer.find(find_word, first_index + 1)
    if search_second_tom == -1:
        print(f'Слово "{find_word}" зустрічається лише один раз — на позиції {first_index}. '
          f'Другого входження в тексті не знайдено.')
    else:
        print(f'Перший раз слово "{find_word}" зустрічається на {first_index} позиції. Але згідно задачі треба знайти точку '
      f'входження слова по тексту вдруге. В даному випадку це станеться на {search_second_tom} позиції. Враховуючи '
      f'довжину слова у {len(find_word)} символів та його позицію входження по тексту вдруге воно закінчиться на '
      f'{search_second_tom + len(find_word) - 1} позиції.')

search_third_tom = adwentures_of_tom_sawer.find(find_word, search_second_tom + 1)
if search_third_tom != -1:
    print (f'Також варто відзначити, що слово "{find_word}" зустрічається по тексту більше ніж два рази')

print()
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
    #print(adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences_four = adwentures_of_tom_sawer_sentences [3]
print(adwentures_of_tom_sawer_sentences_four)
adwentures_of_tom_sawer_sentences_small = adwentures_of_tom_sawer_sentences_four.lower ()
    #print(adwentures_of_tom_sawer_sentences_small)
print()
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
#version 1
find_phrase = 'By the time'
if adwentures_of_tom_sawer.startswith(find_phrase):
    print('(V1) Перше речення уривку починається з фрази "{find_phrase}"')
else:
    if adwentures_of_tom_sawer.find(". By the time"):
        print(f'(V1) В тексті є речення яке починається з фрази "{find_phrase}".')
    else:
        print(f'(V1) В тексті немає речення яке починається з фрази "{find_phrase}".')
print()

#version 2

for sentences in adwentures_of_tom_sawer_sentences:
    if sentences.startswith(find_phrase):
        found = True
        break
if found:
    print (f'(V2) В тексті є речення яке починається з фрази "{find_phrase}".')
else:
    print(f'(V2) В тексті немає речення яке починається з фрази "{find_phrase}".')
print()

#version 3

for sentences in adwentures_of_tom_sawer_sentences:
    if sentences.startswith(find_phrase):
        print('(V3)', True, f'В тексті є речення яке починається з фрази "{find_phrase}".')
print()

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences_last = adwentures_of_tom_sawer_sentences [-1]
    #print(adwentures_of_tom_sawer_sentences_last)
print(f'В останньому реченні запропонованого уривку тексту {len(adwentures_of_tom_sawer_sentences_last.split())} слів.')
