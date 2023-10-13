from searching_framework import *


def manhatten_distance(state, goal):
    x1, y1 = state
    x2, y2 = goal
    return abs(x2 - x1) + abs(y2 - y1)


def maximal_distance(points, given_point):
    if len(points) == 0:
        return 0
    maximum_distance = manhatten_distance(points[0], given_point)
    for point in points:
        maximum_distance = max(manhatten_distance(point, given_point), maximum_distance)
    return maximum_distance


def is_move_valid(snake):
    if snake[0] in snake[1:]:
        return False
    x, y = snake[0]
    return 0 <= x < 10 and 0 <= y < 10


def move_snake_head(movement, body_part, direction):
    x, y = body_part
    new_direction = direction
    south, east, west, north = 'SOUTH', 'EAST', 'WEST', 'NORTH'
    if movement == 'ProdolzhiPravo':
        if direction == south:
            y -= 1
            new_direction = south
        elif direction == north:
            y += 1
            new_direction = north
        elif direction == east:
            x += 1
            new_direction = east
        elif direction == west:
            x -= 1
            new_direction = west
    elif movement == 'SvrtiDesno':
        if direction == south:
            x -= 1
            new_direction = west
        elif direction == north:
            x += 1
            new_direction = east
        elif direction == east:
            y -= 1
            new_direction = south
        elif direction == west:
            y += 1
            new_direction = north
    elif movement == 'SvrtiLevo':
        if direction == south:
            x += 1
            new_direction = east
        elif direction == north:
            x -= 1
            new_direction = west
        elif direction == east:
            y += 1
            new_direction = north
        elif direction == west:
            y -= 1
            new_direction = south

    return (x, y), new_direction


def move_snake(movement, snake, apples, direction):
    casted_snake_position = list(snake)
    casted_apples = list(apples)

    new_snake_position_list = []

    current_snake_head = casted_snake_position[0]
    new_snake_head, new_direction = move_snake_head(movement=movement, body_part=current_snake_head,
                                                    direction=direction)
    new_snake_position_list.append(new_snake_head)
    new_snake_position_list.extend(casted_snake_position[1:])

    new_apple_list = [apple for apple in casted_apples if apple != new_snake_head]
    if new_snake_head in casted_apples:
        old_snake_tail = casted_snake_position[-1]
        new_snake_position_list.append(old_snake_tail)

    return tuple(new_snake_position_list), tuple(new_apple_list), new_direction


class Snake(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        snake_position = state[0]
        green_apples = state[1]
        snake_direction = state[2]

        next_state_dict = {}

        movements = ['ProdolzhiPravo', 'SvrtiDesno', 'SvrtiLevo']
        for movement in movements:
            new_snake_position, new_green_apples, new_direction = move_snake(movement=movement, snake=snake_position,
                                                                             apples=green_apples,
                                                                             direction=snake_direction)
            if is_move_valid(snake=new_snake_position):
                next_state_dict[movement] = new_snake_position, new_green_apples, new_direction
        return next_state_dict

    def goal_test(self, state):
        return len(state[1]) == 0

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        green_apples = node.state[1]
        snake_head = node.state[0][0]
        return maximal_distance(green_apples, snake_head)


if __name__ == '__main__':
    number_of_green_apples = int(input())
    green_apples = [tuple(map(int, input().split(','))) for _ in range(number_of_green_apples)]

    snake_direction = 'SOUTH'
    snake_position = (0, 7), (0, 8), (0, 9)
    initial_state = snake_position, tuple(green_apples), snake_direction
    snake_problem = Snake(initial=initial_state)

    answer = astar_search(snake_problem)
    print(answer.solution())
