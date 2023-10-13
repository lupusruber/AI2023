from searching_framework.uninformed_search import *


def is_move_valid(position, _obstacles):
    x, y = position
    return 0 <= x < 10 and 0 <= y < 10 and position not in _obstacles


def move_pacman(position, pacman_direction, movement):
    casted = list(position)
    movements = ['ProdolzhiPravo', 'ProdolzhiNazad', 'SvrtiLevo', 'SvrtiDesno']

    istok, zapad, sever, jug = 'istok', 'zapad', 'sever', 'jug'
    if pacman_direction == istok:
        if movement == 'FORWARD':
            casted[0] += 1
            new_pacman_direction = istok
            state_movement = movements[0]
        elif movement == 'BACK':
            casted[0] -= 1
            new_pacman_direction = zapad
            state_movement = movements[1]
        elif movement == 'LEFT':
            new_pacman_direction = sever
            casted[1] += 1
            state_movement = movements[2]
        elif movement == 'RIGHT':
            casted[1] -= 1
            new_pacman_direction = jug
            state_movement = movements[3]
    elif pacman_direction == zapad:
        if movement == 'FORWARD':
            casted[0] -= 1
            new_pacman_direction = zapad
            state_movement = movements[0]
        elif movement == 'BACK':
            casted[0] += 1
            new_pacman_direction = istok
            state_movement = movements[1]
        elif movement == 'LEFT':
            new_pacman_direction = jug
            casted[1] -= 1
            state_movement = movements[2]
        elif movement == 'RIGHT':
            casted[1] += 1
            new_pacman_direction = sever
            state_movement = movements[3]
    elif pacman_direction == sever:
        if movement == 'FORWARD':
            casted[1] += 1
            new_pacman_direction = sever
            state_movement = movements[0]
        elif movement == 'BACK':
            casted[1] -= 1
            new_pacman_direction = jug
            state_movement = movements[1]
        elif movement == 'LEFT':
            casted[0] -= 1
            new_pacman_direction = zapad
            state_movement = movements[2]
        elif movement == 'RIGHT':
            casted[0] += 1
            new_pacman_direction = istok
            state_movement = movements[3]
    elif pacman_direction == jug:
        if movement == 'FORWARD':
            casted[1] -= 1
            new_pacman_direction = jug
            state_movement = movements[0]
        elif movement == 'BACK':
            casted[1] += 1
            new_pacman_direction = sever
            state_movement = movements[1]
        elif movement == 'LEFT':
            casted[0] += 1
            new_pacman_direction = istok
            state_movement = movements[2]
        elif movement == 'RIGHT':
            casted[0] -= 1
            new_pacman_direction = zapad
            state_movement = movements[3]

    casted.append(new_pacman_direction)

    return tuple(casted), state_movement


class Pacman(Problem):
    def __init__(self, initial, _obstacles, goal=None):
        super().__init__(initial, goal)
        self.obstacles = _obstacles

    def successor(self, state):
        pacman_position = state[0]
        pacman_position_without_direction = pacman_position[0:2]
        pacman_direction = pacman_position[2]

        list_of_points = list(state[1])

        new_state_dict = {}

        movements = ["FORWARD", "BACK", "LEFT", "RIGHT"]

        for movement in movements:
            new_pacman_position, state_movement = move_pacman(pacman_position_without_direction, pacman_direction,
                                                              movement)
            new_pacman_position_without_direction = new_pacman_position[0:2]

            if is_move_valid(new_pacman_position_without_direction, self.obstacles):
                new_list = [element for element in list_of_points if element != new_pacman_position_without_direction]
                new_state_dict[state_movement] = (new_pacman_position, tuple(new_list))

        return new_state_dict

    def goal_test(self, state):
        return len(state[1]) == 0

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    obstacles = (
        (0, 9), (1, 9), (2, 9), (3, 9), (6, 9), (0, 8), (8, 8), (9, 8), (5, 7), (8, 7), (9, 8), (0, 6), (3, 6), (4, 6),
        (5, 6), (4, 5), (1, 4), (8, 4), (9, 4), (1, 3), (1, 2), (6, 2), (4, 1), (5, 1), (6, 1), (8, 1), (6, 0)
    )
    x_pos = int(input())
    y_pos = int(input())
    direction = input()
    starting_position = (x_pos, y_pos, direction)

    points = []
    n = int(input())
    for _ in range(n):
        string = input().split(",")
        x = int(string[0])
        y = int(string[1])
        points.append((x, y))

    pacman = Pacman(initial=(starting_position, tuple(points)), _obstacles=obstacles)

    result = breadth_first_graph_search(pacman)
    if result is not None:
        print(result.solution())
