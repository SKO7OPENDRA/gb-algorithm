# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

n=abs(int(input('Введите число для перевертыша ')))
l = n
m = 0
while n > 0:
    m = m * 10 + n % 10
    n = n // 10
print(f'Введено  {l}')
print(f'Получено {m}')