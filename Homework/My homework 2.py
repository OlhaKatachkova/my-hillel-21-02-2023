# просим користувача ввести текст
user_text = input('Enter your text')
# текст який вводить користувач
"""Hello, My NaMe is Olha. I want to be a PYTHON PrOgRaMMer!         """

# видаляєм всі небажані знаки пунктуації
user_text = user_text.replace(',', ' ')
user_text = user_text.replace('.', ' ')
user_text = user_text.replace('!', ' ')
user_text = user_text.replace('-', ' ')
user_text = user_text.replace('?', ' ')
user_text = user_text.replace(';', ' ')
user_text = user_text.replace(':', ' ')

#прибираєм зайві пробіли і табуляції
user_text = user_text.rstrip()

#просим користувача ввести слово/словосполучення для заміни
user_text2 = input('What word you want to chang?')

#знаходим індекс вказаного слова/словосполучення
print(input(f'"{user_text2}" was found at position'), user_text.find(f'{user_text2}')       )

#просим користувача ввести слово/словосполучення на яке маєм замінити попередній ввод
user_text3 = input('What word to replace it with?')

#замінюєм дані
user_text = user_text.replace(f'{user_text2}', f'{user_text3}')

#виводим відформатований текст
print(user_text.lower())


