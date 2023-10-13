from searching_framework.uninformed_search import *


class Pacman(Problem):
    def __init__(self, initial, obstacles, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        pass

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[3]) == 0


if __name__ == "__main__":
    pacmanX = int(input())
    pacmanY = int(input())
    direction = input()
    dotsNumber = int(input())

    dots = []
    for i in range(0, dotsNumber):
        dots.append(tuple(map(int, input().split(","))))
    dots = tuple(dots)

    obstacles = [(6, 0), (4, 1), (5, 1), (6, 1), (8, 1), (1, 2), (6, 2), (1, 3),
                 (1, 4), (8, 4), (9, 4), (4, 5), (0, 6), (3, 6), (4, 6), (5, 6),
                 (4, 7), (8, 7), (9, 7), (0, 8), (8, 8), (9, 8), (0, 9), (1, 9),
                 (2, 9), (3, 9), (6, 9)]

    pacman = Pacman((pacmanX, pacmanY, direction, dots), obstacles)

    result = breadth_first_graph_search(pacman)
    print(result.solution())
