import math

from utils import OutputData


def solve(f, start, stop, epsilon):
    if f(start) * f(stop) > 0:
        print("На интервале нет корней или их несколько")
        return None

    x = start
    i = 0
    while abs(start - stop) > epsilon or abs(f(x)) > epsilon:
        x = (start + stop) / 2
        if f(start) * f(x) > 0:
            start = x
        else:
            stop = x
        i += 1
    # x = (start + stop) / 2
    print(abs(start - stop))
    return OutputData(x, f(x), i)
