from data.jacobians import jacobians
from methods import gauss
import numpy


def solve(system, x0, y0):
    errors = [[], []]
    i = 0
    epsilon = 0.01
    inc_x, inc_y = epsilon + 1, epsilon + 1
    while abs(inc_x) > epsilon or abs(inc_y) > epsilon:
        matrix = []
        M1 = numpy.array([[jacobians[system][0][0](x0), jacobians[system][0][1](y0)],
                          [jacobians[system][1][0](x0), jacobians[system][1][1](y0)]])
        v1 = numpy.array([-system[0](x0, y0), -system[1](x0, y0)])
        # for j in range(len(jacobians[system])):
        #     ls = jacobians[system][j]
        #     matrix.append([])
        #     matrix[-1].append(ls[0](x0))
        #     matrix[-1].append(ls[1](y0))
        #     matrix[-1].append(-system[j](x0, y0))

        # print(matrix)
        # inc_x, inc_y = gauss.count_result(matrix)
        # print(inc_x, inc_y)
        inc_x, inc_y = numpy.linalg.solve(M1, v1)

        inc_x = round(inc_x, 3)
        inc_y = round(inc_y, 3)

        print(inc_x, inc_y)

        errors[0].append(inc_x)
        errors[1].append(inc_y)
        x0 += inc_x
        y0 += inc_y

        i += 1

    print("------")
    print(system[0](x0, y0))
    print(system[1](x0, y0))
    print("------")
    print(f'Решение: [{round(x0, 5), round(y0, 5)}]')
    # print(f'Погрешности для х: {errors[0]}')
    # print(f'Погрешности для у: {errors[1]}')
    print(f'Число итераций: {i}')
