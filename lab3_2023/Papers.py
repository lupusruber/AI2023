from constraint import *


def maximum_papers_in_term(*papers_state):
    return papers_state.count('T1') <= 4 and papers_state.count('T2') <= 4 and papers_state.count('T3') <= 4 and papers_state.count('T4') <= 4


def all_in_same_term(*papers_state):

    papers_dict = {'AI': [], 'ML': [], 'NLP': []}

    for index in range(len(papers_state)):
        paper = f'Paper{index + 1}'
        paper_type = papers[paper]
        papers_dict[paper_type].append(papers_state[index])

    for _, value in papers_dict.items():
        if len(value) <= 4:
            if not all(element == value[0] for element in value):
                return False
    return True


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = list(papers.keys())

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(maximum_papers_in_term, variables)
    problem.addConstraint(all_in_same_term, variables)

    result = problem.getSolution()

    # Tuka dodadete go kodot za pechatenje
    list_to_print = [str("%s (%s): %s" % (key, papers[key], result[key])) for key in result.keys()]
    to_change = list_to_print[1]
    list_to_print.remove(to_change)
    list_to_print.append(to_change)
    [print(item) for item in list_to_print]

