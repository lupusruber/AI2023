from constraint import *


def are_attacking(position1, position2):
    x1, y1 = position1
    x2, y2 = position2

    if x1 == x2 or y1 == y2:
        return True

    return abs(x1 - x2) == abs(y1 - y2)


def not_attacking(position1, position2):
    return not are_attacking(position1, position2)


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    n = int(input())

    domain = [(i, j) for i in range(n) for j in range(n)]

    variables = list(range(1, n + 1))
    problem.addVariables(variables, domain)

    [problem.addConstraint(not_attacking, (queen1, queen2)) for queen1 in variables for queen2 in variables if queen1 != queen2]

    if n <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())
