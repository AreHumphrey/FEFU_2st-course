from prettytable import PrettyTable, PLAIN_COLUMNS
from sympy import *


def newton_parameter_minus(t: float, n: int):
    a = 1

    for i in range(n):
        a = a * (t - i)

    a = a / factorial(n)
    return a


def newton_parameter_plus(t: float, n: int):
    a = 1
    for i in range(n):
        a = a * (t + i)

    a = a / factorial(n)

    return a


def gauss1_minus(t: float, n: int):
    a = 1

    for i in range(n):
        if i % 2 == 1 or i == 0:
            a = a * (t - i)
        else:
            a = a * (t + i - 1)

    a = a / factorial(n)
    return a


def gauss2_plus(t: float, n: int):
    a = 1

    for i in range(n):
        if i % 2 == 1 or i == 0:
            a = a * (t + i)
        else:
            a = a * (t - i + 1)

    a = a / factorial(n)
    return a


def insert_gauss1(t: float, n: int, mass: list):
    Px = 0
    j = 5
    for i in range(n):
        Px += mass[i][j] * gauss1_minus(t, i)
        if i % 2 != 0:
            j -= 1
    return Px


def insert_gauss2(t: float, n: int, mass: list):
    Px2 = 0
    j = 5
    for i in range(n):
        Px2 += mass[i][j] * gauss2_plus(t, i)
        if i % 2 == 0:
            j -= 1
    return Px2


def insert_newton1(t: float, n: int, mass: list):
    Px = 0
    j = 0
    for i in range(n):
        Px += mass[i][j] * newton_parameter_minus(t, i)

    return Px


def insert_newton2(t: float, n: int, mass: list):
    Px2 = 0
    for i in range(0, n):
        j = n - i - 1
        Px2 += mass[i][j] * newton_parameter_plus(t, i)

    return Px2


table = PrettyTable()

x = Symbol('x', real=True)
y = x**2 - log(x) - 4
a = 1.5
b = 2.0
h = (b - a) / 10
n = 11

x_star2 = 1.52
x_star3 = 1.52
x_star4 = 1.97

x_list = []
y_list = []
for i in range(0, 11):
    xi = a + i * h
    x_list.append(xi)
    yi = y.subs(x, xi).evalf()
    y_list.append(yi)

table.add_column("№", [i for i in range(0, 11)])
table.add_column("x", x_list)
table.add_column("y(x)", y_list)
print(table)

table.clear()

list_diffs = [y_list.copy()]

while len(list_diffs[-1]) != 1:
    lis = []
    for i in range(0, len(list_diffs[-1]) - 1):
        lis.append(list_diffs[-1][i + 1] - list_diffs[-1][i])
    list_diffs.append(lis)

list_to_table = list_diffs.copy()
max_length = len(max(list_to_table, key=len))

for lst in list_to_table:
    while len(lst) < max_length:
        lst.append("")

table.field_names = ["№", "Value 1", "Value 2", "Value 3", "Value 4", "Value 5", "Value 6", "Value 7", "Value 8",
                     "Value 9", "Value 10", "Value 11"]
for i in range(0, len(list_to_table)):
    table.add_row([f"{i}"] + list_to_table[i])

table.set_style(PLAIN_COLUMNS)
print(table)

t = min(abs(x_list[0] - x_star2), abs(x_list[1] - x_star2)) / h

print('Ньютон 1:', insert_newton1(t, 11, list_diffs))
print("R_N1: ", insert_newton1(t, 11, list_diffs) - y.subs(x, x_star2).evalf())

t = -1 * (x_list[-1] - x_star3) / h

print('Ньютон 2:', insert_newton2(t, 11, list_diffs))
print("R_N2: ", insert_newton2(t, 11, list_diffs) - y.subs(x, x_star3).evalf())

i = 0
for i in range(n - 1):
    if (x_list[i] < x_star4) and (x_list[i + 1] > x_star4):
        break

t1 = abs(x_list[i] - x_star4) / h
t2 = abs(x_list[i + 1] - x_star4) / h

if t1 < t2:
    print('Гаусс 1:', insert_gauss1(t1, 11, list_diffs))
    print("R_G1: ", insert_gauss1(t1, 11, list_diffs) - y.subs(x, x_star4).evalf())
else:
    t2 = -1 * t2
    print('Гаусс 2:', insert_gauss2(t2, 11, list_diffs))
    print("R_G2: ", insert_gauss2(t2, 11, list_diffs) - y.subs(x, x_star4).evalf())

w = 1
for i in range(11):
    w = w * (x - x_list[i])

y_der = diff(y, x, n + 1)
R_n = y_der * w / factorial(n + 1)

crit_points = solve(y_der, x)
crit_points = [point for point in crit_points if a <= float(point) <= b]
endpoints = [a, b]
values_at_endpoints = {endpoint: y_der.subs(x, endpoint).evalf() for endpoint in endpoints}
values_at_critical_points = {cp: y_der.subs(x, cp).evalf() for cp in crit_points}
extremum_values = list(values_at_endpoints.values()) + list(values_at_critical_points.values())
minimum = min(extremum_values)
maximum = max(extremum_values)
print('Минимум f(12)(E) на отрезке:', minimum)
print('Максимум f(12)(E) на отрезке:', maximum)

crit_points = solve(R_n, x)
crit_points = [point for point in crit_points if a <= float(point) <= b]
endpoints = [a, b]
values_at_endpoints = {endpoint: R_n.subs(x, endpoint).evalf() for endpoint in endpoints}
values_at_critical_points = {cp: R_n.subs(x, cp).evalf() for cp in crit_points}
extremum_values = list(values_at_endpoints.values()) + list(values_at_critical_points.values())
minimum = min(extremum_values)
maximum = max(extremum_values)
print('Минимум Rn на отрезке:', minimum)
print('Максимум Rn на отрезке:', maximum)
