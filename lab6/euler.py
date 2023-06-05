import math


def modified_euler(x0, y0, xf, h, f):
    while x0 < xf:
        if x0 + h > xf:
            h = xf - x0
        y0 += (h / 2) * (f(x0, y0) + f(x0 + h, y0 + h * f(x0, y0)))
        x0 += h
    return y0


def solve(f, y0, h, bounds, accuracy):
    n = math.ceil((bounds[1] - bounds[0]) / h) + 1
    x = [bounds[0] + h * i for i in range(n)]

    y = [y0]
    for i in range(len(x) - 1):
        h0 = h
        new_y, r, h0 = do_iteration(f, x, y, h0, i)

        while r >= accuracy:
            new_y, r, h0 = do_iteration(f, x, y, h0, i)
        y.append(new_y)
    return y, x


def do_iteration(f, x, y, h, i):
    y1 = modified_euler(x[i], y[i], x[i + 1], h, f)
    h /= 2
    y2 = modified_euler(x[i], y[i], x[i + 1], h, f)
    r = abs(y1 - y2) / (2 ** 2 - 1)
    return y2, r, h
