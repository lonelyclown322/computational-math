import euler
import miln
from get_data import get_data
from plot import plot_result
from plot import plot_both_results
from runge_kutta import runge_kutta_differentiation


def main():
    f, f_result, initial_conditions, h, bounds, accuracy, method = get_data()
    result_runge_kutta, x = runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy)
    result_euler, x = euler.solve(f, initial_conditions, h, bounds, accuracy)
    result_miln, x = miln.solve(f, initial_conditions, h, bounds, accuracy)
    print("=============results=============")
    print(f"x\t\trunge\t\teuler\t\tmiln\t\treal\t\t")
    for i in range(len(x)):
        print(
            f"{round(x[i], 3)}\t\t{round(result_runge_kutta[i], 5)}\t\t{round(result_euler[i], 5)}\t\t{round(result_miln[i], 5)}\t\t {round(f_result(x[i]), 5)}")
    match method:
        case "Runge–Kutta":
            plot_result([round(f_result(i), 4) for i in x], x, result_runge_kutta, method)
        case "Modified Euler":
            plot_result([round(f_result(i), 4) for i in x], x, result_euler, method)
        case "Miln":
            plot_result([round(f_result(i), 4) for i in x], x, result_miln, method)


main()
