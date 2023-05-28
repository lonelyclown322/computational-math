import numpy

from approximation.tools.standart_deviation import variance, standard_deviation


def square_approximation(points):
    n = len(points)
    x = [dot[0] for dot in points]
    y = [dot[1] for dot in points]

    sum_x = sum(x)
    sum_x2 = sum([xi ** 2 for xi in x])
    sum_x3 = sum([xi ** 3 for xi in x])
    sum_x4 = sum([xi ** 4 for xi in x])
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x2y = sum([(x[i] ** 2) * y[i] for i in range(n)])

    M1 = numpy.array([[n, sum_x, sum_x2],
                      [sum_x, sum_x2, sum_x3],
                      [sum_x2, sum_x3, sum_x4]])

    v1 = numpy.array([sum_y, sum_xy, sum_x2y])

    a_0, a_1, a_2 = numpy.linalg.solve(M1, v1)

    a_0 = round(a_0, 3)
    a_1 = round(a_1, 3)
    a_2 = round(a_2, 3)

    result = {'a_0': a_0, 'a_1': a_1, 'a_2': a_2}

    f = lambda i: a_2 * (i ** 2) + a_1 * i + a_0
    result['function'] = f
    result['string_function'] = f"{a_2}x^2 + {a_1}*x + {a_0}"
    result['variance'] = variance(points, f)
    result['standard_deviation'] = standard_deviation(points, f)

    return result
