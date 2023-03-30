from runge import runge_rule_check


def calculate_simpson(f, a, b, e):
    result_formula = lambda h: simpson_formula(h, a, b, f)
    result, num_of_intervals = runge_rule_check(result_formula, a, b, e * 15)
    print(f"интеграл, посчитанный методом Симпсона={result}, число интервалов={num_of_intervals}")


def simpson_formula(h, a, b, f):
    result = f(a) + f(b)
    n = int((b - a) / h)
    x = a + h
    for i in range(n - 1):
        if i % 2 == 0:
            result += 4 * f(x)
        else:
            result += 2 * f(x)
        x += h
    result *= h / 3
    return result
