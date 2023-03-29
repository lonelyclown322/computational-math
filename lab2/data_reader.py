from pathlib import Path
from data.equations import equation_views, equations, system_of_equations_views, systems_of_equations


class InputData:
    equation = None
    method: int
    system_of_equations = None
    interval: list[float]
    accuracy: float
    x0: float
    y0: float


def input_choice(choices, msg):
    while True:
        try:
            choice = int(input(msg))
            if choice not in choices:
                raise ValueError
            return choice
        except ValueError:
            print("Ошибка, попробуйте еще раз...")


def choose_single_equation():
    for i in range(len(equation_views)):
        print(f'{i + 1}. {equation_views[i]}')
    eq_choice = input_choice(set(range(1, len(equation_views) + 1)), "Введите номер уравнения: ")
    return equations[eq_choice - 1]


def choose_single_system_of_equations():
    for i in range(len(system_of_equations_views)):
        print(f'{i + 1}. {system_of_equations_views[i]}')
    eq_choice = input_choice(set(range(1, len(system_of_equations_views) + 1)),
                             "Введите номер системы уравнений: ")
    return systems_of_equations[eq_choice - 1]


def input_data():
    data = InputData()
    eq_type = input_choice({1, 2}, 'Введите "1" если хотите выбрать уравнение, "2" - систему уравнений: ')
    if eq_type == 1:
        data.equation = choose_single_equation()
        data.method = input_choice({1, 2, 3}, "1. половинного деления\n2. секущей\n3. простых итераций\nВыберите "
                                              "метод: ")
        input_source = input_choice({1, 2},
                                    'Введите "1" если хотите использовать консоль, '
                                    '"2" - файл: ')
        if input_source == 1:
            data.interval = input_interval()
            data.accuracy = input_accuracy()
        elif input_source == 2:
            data.interval, data.accuracy = input_data_from_file()
    elif eq_type == 2:

        data.system_of_equations = choose_single_system_of_equations()
        data.x0, data.y0 = input_approx()

    return data


def input_interval():
    while True:
        try:
            start = float(input("Введите начало интервала: "))
            break
        except ValueError:
            print("Ошибка, попробуйте снова... ")

    while True:
        try:
            end = float(input("Введите конец интервала: "))
            if end <= start:
                print("Конец должен быть больше начала, попробуйте снова...")
                continue
            break
        except ValueError:
            print("Ошибка, попробуйте снова... ")

    return [start, end]


def input_approx():
    while True:
        try:
            x0 = float(input("Введите примерное значение х: "))
            break
        except ValueError:
            print("Ошибка, попробуйте снова")
    while True:
        try:
            y0 = float(input("Введите примерное значение у: "))
            break
        except ValueError:
            print("Ошибка, попробуйте снова")
    return [x0, y0]


def input_accuracy():
    while True:
        try:
            accuracy = float(input("Введите точность: "))
            if accuracy <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка, попробуйте снова")

    return accuracy


def input_data_from_file():
    filename = input("Введите имя файла: ")
    while not Path(filename).is_file():
        filename = input("Файл не найден, попробуйте снова: ")
    with open(filename, "r") as f:
        data = f.read()

        try:
            content = list(map(float, data.split()))
        except ValueError:
            raise ValueError("Ошибка чтения данных из файла")

    if len(content) != 3:
        raise ValueError("Ошибка чтения данных из файла")

    if content[1] < content[0]:
        ValueError("Ошибка чтения данных из файла")

    if content[2] <= 0:
        ValueError("Ошибка чтения данных из файла")

    return [[content[0], content[1]], content[2]]
