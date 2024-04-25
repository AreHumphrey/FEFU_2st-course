import sympy as sp
import math


def func(x):
    return x ** 2 + sp.log(x) - 4


def values(a, b, step):
    table = []
    x = a
    while x <= b:
        table.append((x, func(x)))
        x += step
    return table


def lagrange_polynomial(points, x):
    l = 0
    for i, (x_i, y_i) in enumerate(points):
        l_i = 1
        for j, (x_j, _) in enumerate(points):
            if i != j:
                l_i *= (x - x_j) / (x_i - x_j)
        l += y_i * l_i
    return l


def take_diff(func, x, n):
    new_func = func
    for _ in range(n):
        new_func = sp.diff(new_func, x)
    return new_func


def omega(a, b, step, x):
    res = 1
    while round(a, 2) <= b:
        res *= (x - a)
        a += step
    return res


def main():
    x = sp.symbols('x')
    n = 3
    k = 1
    m = 2
    a = 1.5
    b = 2.0
    step = (b - a) / 3

    points = values(a, b, step)
    print(points)

    L = lagrange_polynomial(points, x)

    print(f"Многочлен Лагранжа: {L}")

    L_diff = sp.diff(L, x)

    f = x ** 2 + sp.log(x) - 4

    d = take_diff(f, x, n)
    df = take_diff(f, x, n)
    r_1 = d.subs(x, 1.5) - L_diff.subs(x, 1.5)
    r_min = (df.subs(x, a) / math.factorial(4)) * omega(a, b, step, x)

    r_max = df.subs(x, b) / math.factorial(4) * omega(a, b, step, x)

    print(f"Производная многочлена Лагранжа: {L_diff}")

    print(L.subs(x, 1.5))

    print(func(1.5).evalf())
    print('----------------------------------------------------------')
    print(L_diff.subs(x, 1.5))
    print(d.subs(x, 1.5))
    print('----------------------------------------------------------')
    print(r_1)
    print(r_min.subs(x, a))
    print(r_max.subs(x, b))


if __name__ == '__main__':
    main()
