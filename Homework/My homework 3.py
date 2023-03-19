#слова які ми визначили як вітання
say_hello_1 = 'hi'
say_hello_2 = 'hello'
say_hello_3 = 'привіт'
say_hello_4 = 'добрий день'
say_hello_5 = 'хай'
x = ''   # вводим х

while not x == (say_hello_1 and say_hello_2 and say_hello_3 and say_hello_4 and say_hello_5):

    x = input()  # призначаєм х значення вводу користувача

#шукаєм перше слово привітання
    if say_hello_1 in x.lower():
        print('Привіт, я бот з України!')
        break
# шукаєм інши слова привітання
    elif say_hello_2 in x.lower():
        print('Привіт, я бот з України!')
        break

    elif say_hello_3 in x.lower():
        print('Привіт, я бот з України!')
        break

    elif say_hello_4 in x.lower():
        print('Привіт, я бот з України!')
        break
    elif say_hello_5 in x.lower():
        print('Привіт, я бот з України!')         #  завершуєм перший цикл якщо виконується якась з даних вимог
        break

    else:
        print('Дуже цікаво, але я не розумію про що йдеться:(')

#слова які ми визначили як запитання користувача
how_are_you_1 = 'що робиш'
how_are_you_2 = 'як справи'
how_are_you_3 = 'чим займаєшся'
x = ''

#починаєм другий цикл
while not x == (how_are_you_1 and how_are_you_2 and how_are_you_3):
    x = input()
    if how_are_you_1 in x.lower():
        print('Вчусь програмувати на Python;)')
        break
    elif how_are_you_2 in x.lower():
        print('Вчусь програмувати на Python;)')
        break
    elif how_are_you_3 in x.lower():
        print('Вчусь програмувати на Python;)')
        break
    else:
        print('Дуже цікаво, але я не розумію про що йдеться:(')

#слова які ми визначили як ключові в третьому циклі
watching_words_1 = 'кіно'
watching_words_2 = 'серіал'
watching_words_3 = 'підкаст'
watching_words_4 = 'шоу'
x = ''

#починаєм третій цикл
while not x == (watching_words_1 and watching_words_2 and watching_words_3 and watching_words_4):
    x = input()

    if watching_words_1 in x.lower():
        print('Соррі, я не в курссі про що мова, але подивіться фільм "Одного разу в Голлівуді", він просто бомба!')
        break
    elif watching_words_2 in x.lower():
        print('Соррі, я не в курссі про що мова, але подивіться фільм "Одного разу в Голлівуді", він просто бомба!')
        break
    elif watching_words_3 in x.lower():
        print('Соррі, я не в курссі про що мова, але подивіться фільм "Одного разу в Голлівуді", він просто бомба!')
        break
    elif watching_words_4 in x.lower():
        print('Соррі, я не в курссі про що мова, але подивіться фільм "Одного разу в Голлівуді", він просто бомба!')
        break
    else:
        print('Дуже цікаво, але я не розумію про що йдеться :(')

#слова які ми визначили як сигнал до завершення чат-бесіди
say_bye_1 = 'good bye'
say_bye_2 = 'до зустрічі'
say_bye_3 = 'гудбай'
say_bye_4 = 'надобриніч'
say_bye_5 = 'бувай'
x = ''

#починаєм останній цикл бесіди
while not x == (say_bye_1 and say_bye_2 and say_bye_3 and say_bye_4 and say_bye_5):
    x = input()

#якщо виконуються цей цикл завершуєм розмову
    if say_bye_1 in x.lower():
        print('Побачимось в мереж, I"ll be back!')
        break
    elif say_bye_2 in x.lower():
        print('Побачимось в мереж, I"ll be back!')
        break
    elif say_bye_3 in x.lower():
        print('Побачимось в мереж, I"ll be back!')
        break
    elif say_bye_4 in x.lower():
        print('Побачимось в мереж, I"ll be back!')
        break
    elif say_bye_5 in x.lower():
        print('Побачимось в мереж, I"ll be back!')
        break
    else:
        print('Дуже цікаво, але я не розумію про що йдеться :(')

















