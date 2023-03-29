from pathlib import Path

from data_reader import input_choice


def output_results(x, func_val, iter_number):
    input_source = input_choice({1, 2}, 'Введите "1" если хотите получит результаты в консоли, "2" - в файле: ')

    if input_source == 1:
        print(f'x = {round(x, 5)}, f(x) = {round(func_val, 5)}, число итераций = {iter_number}')
    elif input_source == 2:
        output_to_file(x, func_val, iter_number)


def output_to_file(x, func_val, iter_number):
    filename = input("Введите имя файла: ")
    while not Path(filename).is_file():
        filename = input("Такого файла не существует, попробуйте снова: ")
    with open(filename, "w") as f:
        print(f'x = {round(x, 5)}, f(x) = {round(func_val, 5)}, число итераций = {iter_number}', file=f)
