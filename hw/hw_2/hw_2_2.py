# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a=int(input('Введите натуральное число: '))
if a<=0:
    print('Я же просил натуральное, а проcто число( Ладно, я сам всё сделаю')
n=abs(a)
print(f'Введено число {a}, я его перешаманил в {n}')
par = impar = 0
while n > 0:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
    n = n // 10
print(f'В числе {n}:', f'четных - {par}, нечетных - {impar}', sep='/n')
