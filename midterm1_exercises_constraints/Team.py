from constraint import *


def get_key_from_value(dict, search):
    for key, value in dict.items():
        if value == search:
            return key


def print_solution(solution):
    print("Total Score: %.1f" % sum(solution.values()))
    for key, value in solution.items():
        if key == leader:
            get_letter = get_key_from_value(dict_of_leaders, value)
            print(f'{key}: {get_letter}')
            continue
        get_letter = get_key_from_value(dict_of_teammates, value)
        print(f'{key}: {get_letter}')


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    n1 = int(input())
    dict_of_teammates = {}
    for _ in range(n1):
        string = input().split(" ")
        dict_of_teammates[string[1]] = float(string[0])

    dict_of_leaders = {}
    n2 = int(input())
    for _ in range(n2):
        string = input().split(" ")
        dict_of_leaders[string[1]] = float(string[0])

    variables = [str(f'Participant {index}') for index in range(1, 6)]
    leader = 'Team leader'

    problem.addVariables(variables, list(dict_of_teammates.values()))
    problem.addVariable(leader, list(dict_of_leaders.values()))

    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(MaxSumConstraint(100))

    solution = problem.getSolutions()

    for _ in solution:
        print_solution(_)

