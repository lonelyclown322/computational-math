import matplotlib.pyplot as plt
import numpy as np
from data.derivatives import derivative
from utils import OutputData

def d(n, x, f, h=0.000001):
    if n <= 0:
        return None
    elif n == 1:
        return (f(x + h) - f(x)) / h

    return (d(n - 1, x + h, f) - d(n - 1, x, f)) / h

def solve(f, start, stop, epsilon):
    if f(start) * f(stop) > 0:
        print("На интервале нет корней или их несколько")
        return None

    l = find_lambda(f, start, stop)
    q = find_q(lambda x: 1 + l * derivative(f)(x), start, stop)

    print(1 + l * derivative(f)(start))
    print(1 + l * derivative(f)(stop))

    # fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    # ax.plot([i for i in np.arange(start, stop, 0.01)], [i + l * f(i) for i in np.arange(start, stop, 0.01)])
    # plt.show()

    # if q >= 1:
    #     print("Не выполнено достаточное условие: q >= 1")
    #     return None

    print(f"lambda={round(l, 5)}, q = {round(q, 5)}")

    phi = lambda x: x + f(x) * l
    print(f"phi(x) = x + f(x)*{round(l, 5)}")

    if q > 0.5:
        check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) > epsilon
    else:
        check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) >= (1 - q) / q * epsilon

    x0 = start

    print("---")
    print(f(start))
    print(d(2, start, f))
    print("----")

    if f(start) * d(2, start, f) > 0:
        x0 = start
    # elif equation(interval[1]) * d(2, interval[1], equation) > 0:
    else:
        x0 = stop


    print(x0 == stop)

    x1 = phi(x0)

    xi = x1
    xi_prev = x0

    i = 0
    # while check(epsilon, xi, xi_prev, q) or abs(f(xi)) > epsilon:
    while abs(f(xi)) > epsilon:

        tmp = xi
        xi = phi(xi)
        xi_prev = tmp
        i += 1
        if i == 100:
            print("check")
            print(check(epsilon, xi, xi_prev, q))
            return OutputData(xi, f(xi), i)

    return OutputData(xi, f(xi), i)


def find_lambda(f, start, stop):
    max_derivative = abs(derivative(f)(start))
    while start < stop:
        if max_derivative < abs(derivative(f)(start)):
            max_derivative = abs(derivative(f)(start))
        start += 0.01
    return -1 / max_derivative


def find_q(f, start, stop):
    max_derivative = abs(f(start))
    while start < stop:
        if max_derivative < abs(f(start)):
            max_derivative = abs(f(start))
        start += 0.01
    print(max_derivative)
    return max_derivative
