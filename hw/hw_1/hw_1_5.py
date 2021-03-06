# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#
# Чтобы определить позицию буквы в алфавите, надо знать по используемой таблице символов коды
# первой буквы алфавита и той, позиция которой определяется. Если вычесть из кода искомой буквы
# код первой и прибавить 1, то получим как раз номер буквы в алфавите. Почему нужно прибавлять 1?
# Представьте, что ищется позиция буквы 'b'. Если из ее кода вычесть код буквы 'a', то получится 1,
# но 'b' - это вторая буква.

# Поиск буквы по ее номеру в алфавите также опирается на знание кода первой буквы.
# К коду первой буквы прибавляется номер в алфавите искомой буквы за вычетом 1.

# Данный код работает с латинскими маленькими буквами.

def return_letter_RUS(number):
    return chr(1039+number)

digit = int(input("Учтите, что буквы Ё тут нет. Введите число от 1 до 32: "))

if digit < 1 or digit > 32:
    print("Нет такой буквы!")
else: print("Буква: " + return_letter_RUS(digit))