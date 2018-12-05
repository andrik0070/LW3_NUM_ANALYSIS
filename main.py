from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np


def bisection_method(a, b, tolerance, max_iter_num, func):
    i = 1
    fa = func(a)
    fp_old = None

    while i <= max_iter_num:
        p = a + (b - a) / 2
        fp_new = func(p)

        # if fp_new == 0 or (i > 1 and (abs(fp_new - fp_old) / abs(fp_new)) < tolerance):
        #     return i, p

        if fp_new == 0 or (b - a)/2 < tolerance:
            return i, p

        i += 1

        if fa * fp_new > 0:
            a = p
            fa = fp_new
        else:
            b = p

        fp_old = fp_new

    raise Exception('Reached max amount of iterations' + str(max_iter_num))


if __name__ == '__main__':
    x = np.linspace(1, 5, 1000, endpoint=True)
    y = []

    func = lambda x: ((np.log(x) ** 2) / x) - 0.22

    for i in x:
        y.append(func(i))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color='red')

    iter_amount, root = bisection_method(1, 5, 0.01, 200, func)

    pprint(iter_amount)
    pprint(root)
    pprint(func(root))

    plt.scatter([root], [func(root)], edgecolors='blue')
    plt.show()
