'''
3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

value_1 = int(input("Введите первое число: "))
value_2 = int(input("Введите второе число: "))
value_3 = int(input("Введите третье число: "))


def my_func(arg_1, arg_2, arg_3):
    if arg_1 < arg_2 and arg_1 < arg_3:
        return arg_2 + arg_3
    elif arg_2 < arg_1 and arg_2 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_1 + arg_2


print(f"Сумма наибольших чисел: {my_func(value_1, value_2, value_3)}")
