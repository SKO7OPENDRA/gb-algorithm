# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

print('Давай сыграем в игру. Нет, не на выживание. Угадай число от 0 до 100. У тебя 10 попыток.',
      'Не угадаешь, PyCharm закроется навсегда. Игра началась! ', sep=('\n'))
m = abs(int(input('Введите число от 0 до 100: ')))
n = 10
while m < 0 or m > 100:
    print('Введено число не от 1 до 100, внимательее!')
    break
while n > 0:
    l = (int(input('Это число ... ')))
    if l > m:    #надо было так грибов наесться, что я написал тут и ниже n, а не m. 10 минут в монитор долбился головой.
        print('Загаданное число меньше.')
    elif l < m:
        print('Загаданное число больше.')
    else:
        print(f'Вы угадали! Это число {m}!',
              'И перед нами победитель! Капитан шоу "Поле программистов". Подарки ... а без подарков сегодня.', sep=('\n'))
        break
    n = n - 1
    print(f'У тебя {n} попыток')
else:
    print(f'Вы проиграли. Я загадывал число {m}',
          'Ладно. На этот раз я не буду закрывать PyCharm. Игра окончена!', sep=('\n'))