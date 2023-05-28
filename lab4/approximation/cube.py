from approximation.tools.standart_deviation import variance, standard_deviation
import numpy as np


def cube_approximation(points):
    n = len(points)
    x = [dot[0] for dot in points]
    y = [dot[1] for dot in points]

    sum_x = sum(x)
    sum_x2 = sum([xi ** 2 for xi in x])
    sum_x3 = sum([xi ** 3 for xi in x])
    sum_x4 = sum([xi ** 4 for xi in x])
    sum_x5 = sum([xi ** 5 for xi in x])
    sum_x6 = sum([xi ** 6 for xi in x])
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x2y = sum([(x[i] ** 2) * y[i] for i in range(n)])
    sum_x3y = sum([(x[i] ** 3) * y[i] for i in range(n)])

    M1 = np.array([[n, sum_x, sum_x2, sum_x3],
                  [sum_x, sum_x2, sum_x3, sum_x4],
                  [sum_x2, sum_x3, sum_x4, sum_x5],
                  [sum_x3, sum_x4, sum_x5, sum_x6]])
    v1 = np.array([sum_y, sum_xy, sum_x2y, sum_x3y])

    a_0, a_1, a_2, a_3 = np.linalg.solve(M1, v1)

    a_0 = round(a_0, 3)
    a_1 = round(a_1, 3)
    a_2 = round(a_2, 3)
    a_3 = round(a_3, 3)

    result = {'a_0': a_0, 'a_1': a_1, 'a_2': a_2, 'a_3': a_3}

    f = lambda i: a_3 * (i ** 3) + a_2 * (i ** 2) + a_1 * i + a_0
    result['function'] = f
    result['string_function'] = f"{a_3}x^3 + {a_2}x^2 + {a_1}*x + {a_0}"
    result['variance'] = variance(points, f)
    result['standard_deviation'] = standard_deviation(points, f)

    return result
