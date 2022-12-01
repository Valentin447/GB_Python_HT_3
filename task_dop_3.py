'''
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением
дробной части элементов.
Пример:
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

numbers_str = input("Введите вещественные числа "
                    "разделенные пробелом: ").split(" ")
numbers_float = []
for i, el in enumerate(numbers_str):
    if float(el) % 1 != 0:
        numbers_float.append(abs(float(el)) % 1)
my_max = numbers_float[0]
my_min = numbers_float[0]
for el in numbers_float:
    if el < my_min and el != 0:
        my_min = el
    elif el > my_max:
        my_max = el
print(f"{round(my_max, 5)} - {round(my_min, 5)} = {round(my_max - my_min, 5)}")
