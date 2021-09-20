"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""
def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2,arg_3]
    term_1 = max(my_list)
    my_list.remove(term_1)
    term_2 = max(my_list)
    result = term_1 + term_2
    return print(result)
my_func(20,30,40)