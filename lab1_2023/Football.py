from searching_framework import *


def is_ball_move_valid(ball, opponents):
    return is_ball_move_valid_tmp(ball, opponents[0]) and is_ball_move_valid_tmp(ball, opponents[1])


def is_ball_move_valid_tmp(ball, opponent):
    x, y = opponent
    return ball not in ((x - 1, y - 1), (x - 1, y), (x, y - 1), (x + 1, y + 1), (x, y + 1), (x + 1, y), (x + 1, y - 1), (x - 1, y + 1)) and 0 <= ball[0] < 8 and 0 <= ball[1] < 6


def move_object(direction, location):
    casted = list(location)
    if direction == "UP":
        casted[1] += 1
    elif direction == "DOWN":
        casted[1] -= 1
    elif direction == "RIGHT":
        casted[0] += 1
    elif direction == "UP_RIGHT":
        casted[0] += 1
        casted[1] += 1
    elif direction == "DOWN_RIGHT":
        casted[0] += 1
        casted[1] -= 1
    return tuple(casted)


def kick_ball(direction, ball_location):
    return move_object(direction, ball_location)


def move_player(direction, player_location):
    return move_object(direction, player_location)


def is_player_move_valid(player, opponents):
    return player not in opponents and 0 <= player[0] < 8 and 0 <= player[1] < 6


class Football(Problem):
    def __init__(self, initial, opponents, goal=None):
        super().__init__(initial, goal)
        self.opponents = opponents

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal

    def successor(self, state):
        new_state_dict = {}
        ball = state[1]
        man = state[0]

        # UP
        up = move_player("UP", man)
        if is_player_move_valid(up, self.opponents):
            if up == ball:
                new_ball = kick_ball("UP", up)
                if is_ball_move_valid(new_ball, self.opponents):
                    new_state_dict["Turni topka gore"] = (up, new_ball)
            else:
                new_state_dict["Pomesti coveche gore"] = (up, ball)

        # DOWN
        down = move_player("DOWN", man)
        if is_player_move_valid(down, self.opponents):
            if down == ball:
                new_ball = kick_ball("DOWN", down)
                if is_ball_move_valid(new_ball, self.opponents):
                    new_state_dict["Turni topka dolu"] = (down, new_ball)
            else:
                new_state_dict["Pomesti coveche dolu"] = (down, ball)

        # RIGHT
        right = move_player("RIGHT", man)
        if is_player_move_valid(right, self.opponents):
            if right == ball:
                new_ball = kick_ball("RIGHT", right)
                if is_ball_move_valid(new_ball, self.opponents):
                    new_state_dict["Turni topka desno"] = (right, new_ball)
            else:
                new_state_dict["Pomesti coveche desno"] = (right, ball)

        # UP RIGHT
        up_right = move_player("UP_RIGHT", man)
        if is_player_move_valid(up_right, self.opponents):
            if up_right == ball:
                new_ball = kick_ball("UP_RIGHT", up_right)
                if is_ball_move_valid(new_ball, self.opponents):
                    new_state_dict["Turni topka gore-desno"] = (up_right, new_ball)
            else:
                new_state_dict["Pomesti coveche gore-desno"] = (up_right, ball)

        # DOWN RIGHT
        down_right = move_player("DOWN_RIGHT", man)
        if is_player_move_valid(down_right, self.opponents):
            if down_right == ball:
                new_ball = kick_ball("DOWN_RIGHT", down_right)
                if is_ball_move_valid(new_ball, self.opponents):
                    new_state_dict["Turni topka dolu-desno"] = (down_right, new_ball)
            else:
                new_state_dict["Pomesti coveche dolu-desno"] = (down_right, ball)

        return new_state_dict


if __name__ == '__main__':
    man_pos = tuple(map(int, input().split(',')))
    ball_pos = tuple(map(int, input().split(',')))
    all_opponents = ((3, 3), (5, 4))
    game = Football((man_pos, ball_pos), all_opponents, goal=((7, 2), (7, 3)))
    result = breadth_first_graph_search(game)
    print(result.solution())
