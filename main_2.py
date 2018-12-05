from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import cmath


def parabol_method(p0, p1, p2, tolerance, max_iter_num, func):
    h1 = p1 - p0
    h2 = p2 - p1

    delta1 = (func(p1) - func(p0)) / h1
    delta2 = (func(p2) - func(p1)) / h2

    d = (delta2 - delta1) / (h2 + h1)
    i = 3

    while i <= max_iter_num:
        b = delta2 + h2 * d
        D = cmath.sqrt(b ** 2 - 4 * func(p2) * d)

        E = b + D if abs(b - D) < abs(b + D) else b - D

        h = -2 * func(p2) / E

        p = p2 + h

        if abs(h) < tolerance:
            return i, p

        p0 = p1
        p1 = p2
        p2 = p

        h1 = p1 - p0
        h2 = p2 - p1
        delta1 = (func(p1) - func(p0)) / h1
        delta2 = (func(p2) - func(p1)) / h2
        d = (delta2 - delta1) / (h2 + h1)

        i += 1

    raise Exception('Reached max amount of iterations' + str(max_iter_num))


if __name__ == '__main__':
    x = np.linspace(1, 5, 100, endpoint=True)
    y = []

    func = lambda x: ((np.log(x) ** 2) / x) - 0.22

    for i in x:
        y.append(func(i))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color='red')

    iter_amount, root = parabol_method(0.5, 1, 1.1, 0.0001, 200, func)

    pprint(iter_amount)
    pprint(root)
    pprint(func(root))

    plt.scatter([root], [func(root)], edgecolors='blue')
    plt.show()
