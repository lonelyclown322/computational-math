import numpy as np
from runge import runge_rule_check


def calculate_trapezoid(f, a, b, e):
    result_formula = lambda h: (sum([f(i) for i in np.arange(a + h, b, h)]) + (f(a) + f(b)) / 2) * h
    integral, num_of_intervals = runge_rule_check(result_formula, a, b, e)
    print(f"интеграл, посчитанный методом трапеции={integral}, число интервалов={num_of_intervals}")
