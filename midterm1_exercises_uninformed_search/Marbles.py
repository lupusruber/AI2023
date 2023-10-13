import math

from searching_framework.uninformed_search import *


def move_marble(position, direction):
    x, y = position
    if direction == 'Gore Levo':
        x -= 1
        y += 1
    elif direction == 'Gore Desno':
        x += 1
        y += 1
    elif direction == 'Dolu Levo':
        x -= 1
        y -= 1
    elif direction == 'Dolu Desno':
        x += 1
        y -= 1
    elif direction == 'Gore':
        y += 1
    elif direction == 'Dolu':
        y -= 1
    elif direction == 'Levo':
        x -= 1
    elif direction == 'Desno':
        x += 1
    return x, y


def is_jump_valid(position, obstacles, list_of_marbles):
    x, y = position
    return 0 <= x < table_size and 0 <= y < table_size and position not in obstacles and position not in list_of_marbles


class Marbles(Problem):
    def __init__(self, initial, obstacles, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def goal_test(self, state):
        return len(state) == 1 and (math.floor(table_size/2), table_size-1) in state

    def successor(self, state):
        new_state_dict = {}

        list_of_marbles = list(state)
        directions = ['Gore Levo', 'Gore Desno', 'Dolu Levo', 'Dolu Desno', 'Gore', 'Dolu', 'Levo', 'Desno']

        for marble in list_of_marbles:
            for direction in directions:
                new_marble = move_marble(marble, direction)
                if new_marble in list_of_marbles:
                    new_jump = move_marble(new_marble, direction)

                    new_list = list_of_marbles.copy()
                    new_list.remove(new_marble)
                    new_list.remove(marble)

                    if is_jump_valid(new_jump, self.obstacles, new_list):
                        x, y = marble
                        new_list.append(new_jump)
                        new_state_dict[f'{direction}: (x={x},y={y})'] = tuple(new_list)

        return new_state_dict

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    table_size = int(input())

    n1 = int(input())
    list_of_marbles = []
    for _ in range(n1):
        string = input().split(',')
        list_of_marbles.append((int(string[0]), int(string[1])))

    n2 = int(input())
    obstacles = []
    for _ in range(n2):
        string = input().split(',')
        obstacles.append((int(string[0]), int(string[1])))

    marbles = Marbles(tuple(list_of_marbles), obstacles)

    result = breadth_first_graph_search(marbles)

    if result is not None:
        print(result.solution())
