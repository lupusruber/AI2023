import math


def euclidean_distance(state, goal):
    x1, y1 = state
    x2, y2 = goal
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def manhatten_distance(state, goal):
    x1, y1 = state
    x2, y2 = goal
    return abs(x2 - x1) + abs(y2 - y1)


def find_closest_point(points, given_point):
    closest_distance = math.inf
    closest_point = points[0]
    for point in points:
        distance = manhatten_distance(point, given_point)
        if distance < closest_distance:
            closest_distance = distance
            closest_point = point
    return closest_point
