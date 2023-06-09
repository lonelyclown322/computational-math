from data.equations import systems_of_equations
from sympy import cos

jacobians = {
    systems_of_equations[0]: [
        [lambda x: 2 * x, lambda y: 2 * y],
        [lambda x: -6 * x, lambda y: 1]
    ],
    systems_of_equations[1]: [
        [lambda x: cos(x), lambda y: 1],
        [lambda x: -6 * x ** 2, lambda y: -4]
    ],
}
