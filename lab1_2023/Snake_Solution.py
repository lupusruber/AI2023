from searching_framework import *


class Snake(Problem):
    def __init__(self, initial, goal, red_apples):
        super().__init__(initial, goal)
        self.red_apples = red_apples

    def check_valid(self, snake_head, snake_body):
        if snake_head in self.red_apples:
            return False
        if snake_head in snake_body:
            return False
        if 0 > snake_head[0] or snake_head[0] > 9 or 0 > snake_head[1] or snake_head[1] > 9:
            return False
        return True

    def move(self, direction, snake, snake_head, apples):
        temp = snake[0]
        new_snake = [snake_head]
        for part in snake[1:]:
            new_snake.append(temp)
            temp = part
        if snake_head in apples:
            new_snake.append(temp)
            return (direction, tuple(new_snake)), tuple([apple for apple in apples if apple != snake_head])
        return (direction, tuple(new_snake)), apples

    def successor(self, state):
        direction, snake, apples = state[0][0], state[0][1], state[1]

        successors = dict()

        if direction == 1:
            # Continue straight
            snake_head = snake[0][0], snake[0][1] + 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, apples)
                successors['ProdolzhiPravo'] = new_state
            # Turn right
            snake_head = snake[0][0] + 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(2, snake, snake_head, apples)
                successors['SvrtiDesno'] = new_state
            # Turn left
            snake_head = snake[0][0] - 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(4, snake, snake_head, apples)
                successors['SvrtiLevo'] = new_state
        elif direction == 2:
            # Continue straight
            snake_head = snake[0][0] + 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, apples)
                successors['ProdolzhiPravo'] = new_state
            # Turn right
            snake_head = snake[0][0], snake[0][1] - 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(3, snake, snake_head, apples)
                successors['SvrtiDesno'] = new_state
            # Turn left
            snake_head = snake[0][0], snake[0][1] + 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(1, snake, snake_head, apples)
                successors['SvrtiLevo'] = new_state
        elif direction == 3:
            # Continue straight
            snake_head = snake[0][0], snake[0][1] - 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, apples)
                successors['ProdolzhiPravo'] = new_state
            # Turn left
            snake_head = snake[0][0] + 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(2, snake, snake_head, apples)
                successors['SvrtiLevo'] = new_state
            # Turn right
            snake_head = snake[0][0] - 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(4, snake, snake_head, apples)
                successors['SvrtiDesno'] = new_state
        else:
            # Continue straight
            snake_head = snake[0][0] - 1, snake[0][1]
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(direction, snake, snake_head, apples)
                successors['ProdolzhiPravo'] = new_state
            # Turn left
            snake_head = snake[0][0], snake[0][1] - 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(3, snake, snake_head, apples)
                successors['SvrtiLevo'] = new_state
            # Turn right
            snake_head = snake[0][0], snake[0][1] + 1
            if self.check_valid(snake_head, snake[:-1]):
                new_state = self.move(1, snake, snake_head, apples)
                successors['SvrtiDesno'] = new_state
        return successors

    def goal_test(self, state):
        return len(state[1]) == 0

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n = int(input())
    zeleni_jabolki = [tuple(map(int, input().split(','))) for _ in range(n)]
    m = int(input())
    crveni_jabolki = [tuple(map(int, input().split(','))) for _ in range(m)]

    nasoka = 3
    zmija = (0, 7), (0, 8), (0, 9)
    sostojba = ((nasoka, zmija), tuple(zeleni_jabolki))
    snake_problem = Snake(sostojba, None, crveni_jabolki)
    answer = breadth_first_graph_search(snake_problem)
    print(answer.solution())
