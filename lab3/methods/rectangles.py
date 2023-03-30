import numpy as np
from runge import runge_rule_check


def calculate_rectangles(f, a, b, e):
    result_start, num_of_intervals_start = count_integral_start(f, a, b, e)
    result_middle, num_of_intervals_middle = count_integral_middle(f, a, b, e)
    result_stop, num_of_intervals_stop = count_integral_stop(f, a, b, e)
    print(
        f"интеграл, посчитанный методом прямоугольников (начало)={result_start},"
        f" число интервалов={num_of_intervals_start}")
    print(
        f"интеграл, посчитанный методом прямоугольников (середина)={result_middle},"
        f" число интервалов={num_of_intervals_middle}")
    print(
        f"интеграл, посчитанный методом прямоугольников (конец)={result_stop},"
        f" число интервалов={num_of_intervals_stop}")


def count_integral_start(f, a, b, e):
    result_start = lambda h: sum([f(i) for i in np.arange(a, b - h, h)]) * h
    return runge_rule_check(result_start, a, b, e)


def count_integral_middle(f, a, b, e):
    result_start = lambda h: sum([f(i) for i in np.arange(a + h / 2, b, h)]) * h
    return runge_rule_check(result_start, a, b, e)


def count_integral_stop(f, a, b, e):
    result_start = lambda h: sum([f(i) for i in np.arange(a + h, b, h)]) * h
    return runge_rule_check(result_start, a, b, e)
