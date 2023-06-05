from decimal import Decimal
from math import ceil


def runge_kutta(x0, y0, xf, h, f):
    while x0 < xf:
        if x0 + h > xf:
            h = xf - x0
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * f(x0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x0 += h
    return y0


def runge_kutta_differentiation(f, initial_conditions, h, bounds, e):
    n = ceil((bounds[1] - bounds[0]) / h) + 1
    x = [bounds[0] + h * i for i in range(n)]
    y = [0] * n
    y[0] = initial_conditions

    for i in range(n - 1):
        h0 = h
        a = x[i]
        b = x[i + 1]
        y0 = y[i]
        y1, R, h0 = do_iteration(h0, a, b, y0, f, e)
        counter = 0
        while R >= e:
            counter += 1
            y1, R, h0 = do_iteration(h0, a, b, y0, f, e)
        y[i + 1] = y1
    return y, x


def do_iteration(h0, a, b, y0, f, e):
    y1 = runge_kutta(a, y0, b, h0, f)
    h0 /= 2
    y2 = runge_kutta(a, y0, b, h0, f)
    R = abs(y1 - y2) / (2 ** (-fexp(e)) - 1)
    return y1, R, h0


def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1
