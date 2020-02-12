'''
Система счисления

10 - 42
2  - 0b101010
8  - 0o52
16 - 0x2a

|10|2   |8 |16|
+--+----+--+--+
|0 |   0|0 |0 |
|1 |   1|1 |1 |
|2 |  10|2 |2 |
|3 |  11|3 |3 |
|4 | 100|4 |4 |
|5 | 101|5 |5 |
|6 | 110|6 |6 |
|7 | 111|7 |7 |
|8 |1000|10|8 |
|9 |1001|11|9 |
|10|1010|12|A |
|11|1011|13|B |
|12|1100|14|C |
|13|1101|15|D |
|14|1110|16|E |
|15|1111|17|F |
'''

a = 42
print(a)        # в десятичной
print(bin(a))   # в двоичной
print(oct(a))   # в восьмеричной
print(hex(a))   # в шестнадцатеричной

b = 0b100110
print(b)    # Выводит b в десятеричной системе
# в Python можно использовать любый числа от двиочной до тридцатишестиричной систем

c = int('2cd50', base=24)
print(c) # 837048

z = int('z', base=36) # z можно использовать только в 36-ричной системе. Иначе ошибка
print(z) # 35

'''
Целые числа в двоичном коде
Прямой  | 12|0|0|0|0|1|1|0|0| 
Обратный|-12|1|1|1|1|0|0|1|1|
Дополнит|-12|1|1|1|1|0|1|0|0| Надо к обратному порядку прибавить 1 бит
'''

'''
Вещественные числа в двоичном коде
312,3125 == 100111000,0101
Сдвигаем строку так, чтобы в начале осталась одна единица
100111000,0101 == 1,001110000101*2^8 == 1,001110000101*10^1000 (полностью в двоичной системе)
8-я степень (или 1000) - порядок числа
А само число 1,001110000101 - называется мантисой
При работе с вещественными числами, мантиса округляется, так как мантиса имеет ограниченный размер.
Все знаки, которые не влезли в мантису отбрасываются.
'''

# ord - получает код символа
print(ord('d')) # 100
print(ord('л')) # 1083
# 1083 - не кодировка ASCII, у которой 255 символов
# python сам определяет кодировку и выделяет 1, 2, 4 или 8 байт н а хранение буквы