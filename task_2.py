"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""
def user_data():
    name = input('Введите ваше имя: ')
    surname = input('Введите вашу фамилю: ')
    city = input('Введите ваш город: ')
    e_mail = input('Введите ваш E-Mail: ')
    number = input('Введите номер вашего телефона: ')
    result = print(f"Вас зовут {name} {surname}. Вы из города {city}. Ваши контакты {e_mail}, {number}.")
    return result
result = user_data()
print(result)
