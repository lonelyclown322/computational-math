from runge_kutta import runge_kutta_differentiation
from math import ceil


def solve(f, initial_conditions, h, bounds, accuracy):
    n = ceil((bounds[1] - bounds[0]) / h) + 1
    if n < 4:
        return None

    x = [bounds[0] + h * i for i in range(n)]

    runge_result, runge_x = runge_kutta_differentiation(f, initial_conditions, h, [x[0], x[3]], accuracy)

    y = runge_result[:4]

    for i in range(4, n):
        y_prediction = prediction(h, f, x, y, i)
        y_correction = correction(h, f, x, y, i, y_prediction)

        while abs(y_correction - y_prediction) > accuracy:
            y_prediction = y_correction
            y_correction = correction(h, f, x, y, i, y_prediction)
        y.append(y_correction)

    return y, x


def prediction(h, f, x, y, i):
    tmp = 2 * f(x[i - 3], y[i - 3]) - f(x[i - 2], y[i - 2]) + 2 * f(x[i - 1], y[i - 1])
    return y[i - 4] + 4 * h * tmp / 3


def correction(h, f, x, y, i, y_pred):
    tmp = f(x[i - 2], y[i - 2]) + 4 * f(x[i - 1], y[i - 1]) + f(x[i], y_pred)
    return y[i - 2] + h * tmp / 3