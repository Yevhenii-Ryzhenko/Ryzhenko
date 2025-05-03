while True:
    print('Введіть у поле нижче слово, яке містить літеру "h або "H')
    user_text = input()
    if 'h' in user_text.lower():
        print(f'Дякую. Ваше слово "{user_text}" містить необхідну літеру та підходить')
        break
    else:
        print(f'Введене слово "{user_text}" не містить літери "h" або "H". Спробуйте ще раз.')
