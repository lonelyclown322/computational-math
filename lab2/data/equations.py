from sympy import cos
from sympy import sin

equations = [
    lambda x: x ** 3 - x + 4,
    lambda x: 2 * cos(2 * x) + 3 * sin(x),
    lambda x: 4 * x ** 3 + 20 * x ** 2 + 1,
]

equation_views = [
    "x^3 - x + 4",
    "2cos(2x) + 3sin(x)",
    "4x^3 + 20x^2 + 1",
]

systems_of_equations = [
    tuple([lambda x, y: x ** 2 + y ** 2 - 4, lambda x, y: y - 3 * x ** 2]),
    tuple([lambda x, y: sin(x) + y - 1, lambda x, y: -2 * x ** 3 - 4 * y + 5]),
]

system_of_equations_views = [
    "{ x^2 + y^2 - 4,\n     y - 3x^2 }",
    "{ sin(x) + y - 1,\n     -2x^3 - 4y + 5 }"
]
