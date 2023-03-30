def runge_rule_check(result_formula, a, b, e):
    num_of_intervals = 10
    h = interval_width(a, b, num_of_intervals)

    result = result_formula(h)
    prev_result = result + 1

    print("знач при н = 10")
    print(result)

    while abs(result - prev_result) > e:
        num_of_intervals *= 2
        h = interval_width(a, b, num_of_intervals)
        prev_result = result
        result = result_formula(h)
    return result, num_of_intervals


def interval_width(a, b, num_of_intervals):
    return abs(b - a) / num_of_intervals
