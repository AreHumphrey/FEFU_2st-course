import numpy as np
from prettytable import PrettyTable


def function(x):
    return 2 ** x - 2 * x ** 2 - 1


def derivative_function(x):
    return 2 ** x * np.log(2) - 4 * x


def chord_method(eps, lst: list):
    table = PrettyTable()
    table.field_names = ["Итерация", "Значение x"]

    counter = 1
    b = lst[1]
    x_prev = lst[0]
    x_next = x_prev - (b - x_prev) * function(x_prev) / (function(b) - function(x_prev))
    table.add_row([counter, x_next])

    while abs(x_next - x_prev) > eps:
        x_prev = x_next
        x_next = x_prev - (b - x_prev) * function(x_prev) / (function(b) - function(x_prev))
        counter += 1
        print(x_next)
        table.add_row([counter, x_next])

    print(table.get_string(border=True, header=False, hrules=1))
    return x_next


def newton_method(eps, x0):
    table = PrettyTable()
    table.field_names = ["Итерация", "Значение x"]

    count = 1
    x_prev = x0
    x_next = x_prev - function(x_prev) / derivative_function(x_prev)
    table.add_row([count, x_next])

    while abs(x_next - x_prev) > eps:
        count += 1
        x_prev = x_next
        x_next = x_prev - function(x_prev) / derivative_function(x_prev)
        print(x_next)
        table.add_row([count, x_next])
    print(table.get_string(border=True, header=False, hrules=1))
    return x_next


def bisection_method(eps, lst: list):
    l = lst[0]
    r = lst[1]
    c = 0
    count = 1

    x_prev = r
    x_next = c

    while abs(x_next - x_prev) > eps:
        c = (r + l) / 2

        if function(c) * function(l) > 0:
            l = c
        elif function(c) * function(r) > 0:
            r = c

        x_prev = x_next
        x_next = c
        print(count, x_next)
        count += 1

    return x_next


print("Метод хорд:")
chord_method(0.0000001, [0.3, 1.5])

print("\n Метод Ньютона:")
newton_method(0.0000001, 1.5)

print("\n Метод бисекции:")
bisection_method(0.0000001, [0.5, 1.5])
