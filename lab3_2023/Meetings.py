from constraint import *


def valid_Simona(attendance, term_for_other):
    return attendance == 1 and term_for_other in available_terms_Simona


def valid_Petar(attendance, term_for_other):
    if attendance == 1 and term_for_other in available_terms_Petar:
        return True
    return attendance == 0 and term_for_other in available_terms_Marija


def valid_Marija(attendance, term_for_other):
    if attendance == 1 and term_for_other in available_terms_Marija:
        return True
    return attendance == 0 and term_for_other in available_terms_Petar


if __name__ == '__main__':
    problem = Problem(RecursiveBacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 20))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    available_terms_Simona = [13, 14, 16, 19]
    available_terms_Marija = [14, 15, 18]
    available_terms_Petar = [12, 13, 16, 17, 18, 19]
    problem.addConstraint(valid_Simona, ['Simona_prisustvo', 'vreme_sostanok'])
    problem.addConstraint(valid_Petar, ['Petar_prisustvo', 'vreme_sostanok'])
    problem.addConstraint(valid_Marija, ['Marija_prisustvo', 'vreme_sostanok'])

    # ----------------------------------------------------

    for solution in problem.getSolutions():
        print("{'Simona_prisustvo': " + str(solution["Simona_prisustvo"]) + ", 'Marija_prisustvo': " +
              str(solution["Marija_prisustvo"]) + ", 'Petar_prisustvo': " +
              str(solution["Petar_prisustvo"]) + ", 'vreme_sostanok': " + str(solution["vreme_sostanok"]) + "}")
