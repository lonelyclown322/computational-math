from utils import OutputData


def d(n, x, f, h=0.00000001):
    if n <= 0:
        return None
    elif n == 1:
        return (f(x + h) - f(x)) / h

    return (d(n - 1, x + h, f) - d(n - 1, x, f)) / h


def solve(equation, interval, accuracy):
    if equation(interval[0]) * equation(interval[1]) > 0:
        print("На интервале нет корней или их несколько")
        return None

    if equation(interval[0]) * d(2, interval[0], equation) > 0:
        previous_x = interval[0]
    # elif equation(interval[1]) * d(2, interval[1], equation) > 0:
    else:
        previous_x = interval[1]
    # else:
    #     print(
    #         "Не выполняется достаточное условие: знаки второй производной и функции разные как на начале интервала, "
    #         "так и в конце ")
    #     return None

    print(previous_x)

    current_x = previous_x + 0.03

    next_x = current_x - equation(current_x) * (current_x - previous_x) / (
            equation(current_x) - equation(previous_x))

    current_iteration = 1
    # max_iteration = 100000

    while abs(next_x - current_x) > accuracy or equation(current_x) > accuracy:
        previous_x = current_x
        current_x = next_x
        next_x = current_x - equation(current_x) * (current_x - previous_x) / (
                equation(current_x) - equation(previous_x))

        current_iteration += 1

    # if current_iteration == max_iteration or (next_x > interval[1] or next_x < interval[0]):
    #     print("На заданном интервале нет корней")
    #     return None

    return OutputData(next_x, equation(next_x), current_iteration)
