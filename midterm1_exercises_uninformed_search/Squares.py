from searching_framework.uninformed_search import *


def is_movement_valid(position, position_of_squares):
    x, y = position
    return 0 <= x < 5 and 0 <= y < 5 and position_of_squares.count(position) <= 1


def move_square(position, direction):
    casted = list(position)
    if direction == "gore":
        casted[1] += 1
    elif direction == "dolu":
        casted[1] -= 1
    elif direction == 'levo':
        casted[0] -= 1
    elif direction == "desno":
        casted[0] += 1
    return tuple(casted)


class Squares(Problem):
    def __init__(self, initial, house):
        super().__init__(initial, house)

    def goal_test(self, state):
        return state == self.goal

    def successor(self, state):
        new_state_dict = {}
        list_of_squares = list(state)

        directions = ['gore', 'dolu', 'desno', 'levo']

        for index, square in enumerate(list_of_squares):
            for direction in directions:
                new_square = move_square(square, direction)
                if is_movement_valid(new_square, list_of_squares):
                    new_list_of_squares = list_of_squares.copy()
                    new_list_of_squares[index] = new_square
                    new_state_dict[f'Pomesti kvadratche {index + 1} {direction}'] = tuple(new_list_of_squares)

        return new_state_dict

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    initial_state = tuple()
    for _ in range(5):
        initial_state += (tuple(map(int, input().split(','))), )

    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(initial_state, goal_state)

    result = breadth_first_graph_search(squares)

    if result is not None:
        print(result.solution())
