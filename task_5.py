"""Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce

created_list = [element for element in range(100, 1001) if element % 2 == 0]


def reducer_func(el_prev, el):
    return el_prev + el


print(reduce(reducer_func, created_list))
