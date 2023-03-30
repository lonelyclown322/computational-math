import math


def choose_equation():
    print("Выберите одно из трех уравнений:")
    print("1)  sin(x)")
    print("2)  -x^3 +  7*x^2 - 3*x - 2")
    print("3)  2 * x ** 3 - 9 * x ** 2 - 7 * x + 11")

    match int(input()):
        case 1:
            equation = lambda x: math.sin(x)
        case 2:
            equation = lambda x: -x ** 3 + 7 * x ** 2 - 3 * x - 2
        case 3:
            equation = lambda x: 2 * x ** 3 - 9 * x ** 2 - 7 * x + 11
    return equation


def choose_interval():
    print("Введите начало интервала")
    start = float(input())
    print("Введите конец интервала")
    stop = float(input())

    if stop <= start:
        print("Ошибка! Конец должен быть больше начала!")
        return choose_interval()
    else:
        return start, stop


def choose_accuracy():
    print("Введите точность:")
    return float(input())


def choose_method():
    print("Выберите метод для вычисления интеграла:")
    print("1) метод трапеций")
    print("2) метод прямоугольников")
    print("3) метод Симпсона")
    return int(input())
