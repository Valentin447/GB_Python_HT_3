'''
2) Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры
как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

my_first_name = input("Введите имя: ")
my_last_name = input("Введите фамилию: ")
my_year = input("Введите год рождения: ")
my_city = input("Введите город проживания: ")
my_email = input("Введите email: ")
my_phone = input("Введите телефон: ")


def print_data(first_name, last_name, year, city, email, phone):
    print(f"Имя: {first_name}; Фамилия: {last_name}; Год рождения: {year}; "
          f"Город проживания: {city}; Email: {email}; Tелефон: {phone}")


print_data(first_name=my_first_name, last_name=my_last_name, year=my_year,
           city=my_city, email=my_email, phone=my_phone)
