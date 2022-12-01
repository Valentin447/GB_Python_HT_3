'''
1) Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''

dividend = int(input("Введите делимое: "))
divisor = int(input("Введите делитель: "))


def my_divide(x, y):
    try:
        return round(x / y, 2)
    except ZeroDivisionError:
        print(f"Нельзя делить на ноль!")


print(f"{dividend} / {divisor} = {my_divide(dividend, divisor)}")
