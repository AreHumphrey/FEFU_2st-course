from math import factorial, log

import pandas as pd
from tabulate import tabulate


def func(x):
    return x ** 2 + log(x) - 4


def f_derivative(x, k):
    if k == 1:
        return 2 * x + 1 / x
    elif k == 2:
        return 2 - 1 / x ** 2
    return (-1) ** ((k % 2) + 1) * factorial(k - 1) / x ** k


def middle_rectangular(func, a, b, n):
    h = (b - a) / n
    return sum(func(a + h * (i + 0.5)) * h for i in range(n))


def mr_error(func, a, b, n):
    m = max(abs(f_derivative(a + (b - a) * i / 1000, 2)) for i in range(1001))
    return m / 24 * (b - a) ** 3 / n ** 2


a, b = 1.5, 2
n = 1
I = -0.180236634376

result = {'j': [], 'n': [], 'I_n': [], 'delta_I_n': [], 'relative_I_n': [],
          'R_n': [], 'growth': [0]}
for i in range(15):
    n *= 2
    I_n = middle_rectangular(func, a, b, n)
    result['j'].append(i + 1)
    result['n'].append(n)
    result['I_n'].append(I_n)
    result['delta_I_n'].append(abs(I - I_n))
    result['relative_I_n'].append(result['delta_I_n'][i] / abs(I) * 100)
    result['R_n'].append(mr_error(func, a, b, n))
    if i > 0:
        result['growth'].append(result['delta_I_n'][i] / result['delta_I_n'][i - 1])


def left_rectangular(func, a, b, n):
    h = (b - a) / n
    return sum(func(a + h * i) * h
               for i in range(n))


def right_rectangular(func, a, b, n):
    h = (b - a) / n
    return sum(func(a + h * i)
               for i in range(1, n + 1)) * h


def trapezoidal(func, a, b, n):
    h = (b - a) / n
    return ((func(a) + func(b)) / 2 + sum(func(a + h * i)
                                          for i in range(1, n))) * h


def simpson(func, a, b, n):
    h = (b - a) / n
    return sum(func(a + h * (i - 1)) + 4 * func(a + h * (i - 0.5)) + func(a + h * (i))
               for i in range(1, n + 1)) * h / 6


def l_rect_error(func, a, b, n):
    m = max(abs(f_derivative(a + (b - a) * i / 1000, 1)) for i in range(1001))
    return m * (b - a) / 2


def r_rect_error(func, a, b, n):
    m = max(abs(f_derivative(a + (b - a) * i / 1000, 1)) for i in range(1001))
    return m * (b - a) / 2


def trapezoidal_error(func, a, b, n):
    m = max(abs(f_derivative(a + (b - a) * i / 1000, 2)) for i in range(1001))
    return m / 12 * (b - a) ** 3 / n ** 2


def simpson_error(func, a, b, n):
    m = max(abs(f_derivative(a + (b - a) * i / 1000, 4)) for i in range(1001))
    return m / 2880 * (b - a) ** 5 / n ** 4


df_middle_rect = pd.DataFrame({
    'Iteration': result['j'],
    'n': result['n'],
    'I_n': result['I_n'],
    'delta_I_n': result['delta_I_n'],
    'Relative Error (%)': result['relative_I_n'],
    'R_n': result['R_n'],
    'Growth': result['growth']
})

print("Таблица значений для метода центральных прямоугольников:")
print(df_middle_rect)


calculate = {'method': ['Левых прямоугольников', "Правих прямоугольников",
                        "Центральных прямоугольников", "Трапеций", "Симпсона"],
             'I_n': [], 'delta_I_n': [], 'relative_I_n': [], 'R_n': []}
for i, (formula, error) in enumerate([(left_rectangular, l_rect_error), (right_rectangular, r_rect_error),
                                      (middle_rectangular, mr_error), (trapezoidal, trapezoidal_error),
                                      (simpson, simpson_error)]):
    calculate['I_n'].append(formula(func, a, b, 10000))
    calculate['delta_I_n'].append(abs(I - calculate['I_n'][i]))
    calculate['relative_I_n'].append(calculate['delta_I_n'][i] / abs(I) * 100)
    calculate['R_n'].append(error(func, a, b, 10000))

table_headers = ['Method', 'I_n', 'delta_I_n', 'relative_I_n', 'R_n']
table_data = [["Левых прямоугольников", calculate['I_n'][0], calculate['delta_I_n'][0], calculate['relative_I_n'][0],
               calculate['R_n'][0]],
              ["Правих прямоугольников", calculate['I_n'][1], calculate['delta_I_n'][1], calculate['relative_I_n'][1],
               calculate['R_n'][1]],
              ["Центральных прямоугольников", calculate['I_n'][2], calculate['delta_I_n'][2],
               calculate['relative_I_n'][2],
               calculate['R_n'][2]],
              ["Трапеций", calculate['I_n'][3], calculate['delta_I_n'][3], calculate['relative_I_n'][3],
               calculate['R_n'][3]],
              ["Симпсона", calculate['I_n'][4], calculate['delta_I_n'][4], calculate['relative_I_n'][4],
               calculate['R_n'][4]]]

print(tabulate(table_data, headers=table_headers, tablefmt='grid'))
