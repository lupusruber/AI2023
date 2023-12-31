from sklearn.tree import DecisionTreeClassifier


def get_dataset():
    return [[6.3, 2.3, 4.4, 1.3, 2],
            [6.4, 2.8, 5.6, 2.1, 0],
            [5.1, 3.3, 1.7, 0.5, 1],
            [5.1, 3.5, 1.4, 0.2, 1],
            [4.6, 3.1, 1.5, 0.2, 1],
            [5.8, 2.7, 5.1, 1.9, 0],
            [5.5, 3.5, 1.3, 0.2, 1],
            [5.7, 2.6, 3.5, 1.0, 2],
            [5.0, 3.5, 1.3, 0.3, 1],
            [6.3, 2.5, 5.0, 1.9, 0],
            [6.2, 2.2, 4.5, 1.5, 2],
            [5.0, 3.4, 1.6, 0.4, 1],
            [5.7, 4.4, 1.5, 0.4, 1],
            [4.9, 2.4, 3.3, 1.0, 2],
            [4.4, 2.9, 1.4, 0.2, 1],
            [5.5, 2.4, 3.7, 1.0, 2],
            [5.6, 2.5, 3.9, 1.1, 2],
            [5.6, 2.8, 4.9, 2.0, 0],
            [4.8, 3.4, 1.6, 0.2, 1],
            [5.6, 3.0, 4.5, 1.5, 2],
            [6.0, 3.0, 4.8, 1.8, 0],
            [6.3, 3.3, 4.7, 1.6, 2],
            [4.8, 3.0, 1.4, 0.1, 1],
            [7.9, 3.8, 6.4, 2.0, 0],
            [4.9, 3.0, 1.4, 0.2, 1],
            [4.3, 3.0, 1.1, 0.1, 1],
            [6.8, 3.2, 5.9, 2.3, 0],
            [5.6, 2.7, 4.2, 1.3, 2],
            [5.2, 4.1, 1.5, 0.1, 1],
            [6.2, 2.9, 4.3, 1.3, 2],
            [6.5, 2.8, 4.6, 1.5, 2],
            [5.4, 3.9, 1.3, 0.4, 1],
            [5.8, 2.6, 4.0, 1.2, 2],
            [5.4, 3.7, 1.5, 0.2, 1],
            [4.5, 2.3, 1.3, 0.3, 1],
            [6.3, 3.4, 5.6, 2.4, 0],
            [6.2, 3.4, 5.4, 2.3, 0],
            [5.7, 2.5, 5.0, 2.0, 0],
            [5.8, 2.7, 3.9, 1.2, 2],
            [6.4, 2.7, 5.3, 1.9, 0],
            [5.1, 3.8, 1.6, 0.2, 1],
            [6.3, 2.5, 4.9, 1.5, 2],
            [7.7, 2.8, 6.7, 2.0, 0],
            [5.1, 3.5, 1.4, 0.3, 1],
            [6.8, 2.8, 4.8, 1.4, 2],
            [6.1, 3.0, 4.6, 1.4, 2],
            [5.5, 4.2, 1.4, 0.2, 1],
            [5.0, 2.0, 3.5, 1.0, 2],
            [7.7, 3.0, 6.1, 2.3, 0],
            [5.1, 2.5, 3.0, 1.1, 2],
            [5.9, 3.0, 5.1, 1.8, 0],
            [7.2, 3.2, 6.0, 1.8, 0],
            [4.9, 3.1, 1.5, 0.2, 1],
            [5.7, 3.0, 4.2, 1.2, 2],
            [6.1, 2.9, 4.7, 1.4, 2],
            [5.0, 3.2, 1.2, 0.2, 1],
            [4.4, 3.2, 1.3, 0.2, 1],
            [6.7, 3.1, 5.6, 2.4, 0],
            [4.6, 3.6, 1.0, 0.2, 1],
            [5.1, 3.4, 1.5, 0.2, 1],
            [5.2, 2.7, 3.9, 1.4, 2],
            [6.4, 3.1, 5.5, 1.8, 0],
            [7.4, 2.8, 6.1, 1.9, 0],
            [4.9, 3.1, 1.5, 0.1, 1],
            [5.0, 3.5, 1.6, 0.6, 1],
            [6.7, 3.1, 4.7, 1.5, 2],
            [6.4, 3.2, 5.3, 2.3, 0],
            [6.3, 2.7, 4.9, 1.8, 0],
            [5.8, 4.0, 1.2, 0.2, 1],
            [6.9, 3.1, 5.4, 2.1, 0],
            [5.9, 3.2, 4.8, 1.8, 2],
            [6.6, 2.9, 4.6, 1.3, 2],
            [6.1, 2.8, 4.0, 1.3, 2],
            [7.7, 2.6, 6.9, 2.3, 0],
            [5.5, 2.6, 4.4, 1.2, 2],
            [6.3, 2.9, 5.6, 1.8, 0],
            [7.2, 3.0, 5.8, 1.6, 0],
            [6.5, 3.0, 5.8, 2.2, 0],
            [5.4, 3.9, 1.7, 0.4, 1],
            [6.5, 3.2, 5.1, 2.0, 0],
            [5.9, 3.0, 4.2, 1.5, 2],
            [5.1, 3.7, 1.5, 0.4, 1],
            [5.7, 2.8, 4.5, 1.3, 2],
            [5.4, 3.4, 1.5, 0.4, 1],
            [4.6, 3.4, 1.4, 0.3, 1],
            [4.9, 3.6, 1.4, 0.1, 1],
            [6.7, 2.5, 5.8, 1.8, 0],
            [5.0, 3.6, 1.4, 0.2, 1],
            [6.7, 3.3, 5.7, 2.5, 0],
            [4.4, 3.0, 1.3, 0.2, 1],
            [6.0, 2.2, 5.0, 1.5, 0],
            [6.0, 2.2, 4.0, 1.0, 2],
            [5.0, 3.4, 1.5, 0.2, 1],
            [5.7, 2.8, 4.1, 1.3, 2],
            [5.5, 2.4, 3.8, 1.1, 2],
            [5.1, 3.8, 1.9, 0.4, 1],
            [6.9, 3.1, 5.1, 2.3, 0],
            [5.6, 2.9, 3.6, 1.3, 2],
            [6.1, 2.8, 4.7, 1.2, 2],
            [5.5, 2.5, 4.0, 1.3, 2],
            [5.5, 2.3, 4.0, 1.3, 2],
            [6.0, 2.9, 4.5, 1.5, 2],
            [5.1, 3.8, 1.5, 0.3, 1],
            [5.7, 3.8, 1.7, 0.3, 1],
            [6.7, 3.3, 5.7, 2.1, 0],
            [4.8, 3.1, 1.6, 0.2, 1],
            [5.4, 3.0, 4.5, 1.5, 2],
            [6.5, 3.0, 5.2, 2.0, 0],
            [6.8, 3.0, 5.5, 2.1, 0],
            [7.6, 3.0, 6.6, 2.1, 0],
            [5.0, 3.0, 1.6, 0.2, 1],
            [6.7, 3.0, 5.0, 1.7, 2],
            [4.8, 3.4, 1.9, 0.2, 1],
            [5.8, 2.8, 5.1, 2.4, 0],
            [5.0, 2.3, 3.3, 1.0, 2],
            [4.8, 3.0, 1.4, 0.3, 1],
            [5.2, 3.5, 1.5, 0.2, 1],
            [6.1, 2.6, 5.6, 1.4, 0],
            [5.8, 2.7, 4.1, 1.0, 2],
            [6.9, 3.2, 5.7, 2.3, 0],
            [6.4, 2.9, 4.3, 1.3, 2],
            [7.3, 2.9, 6.3, 1.8, 0],
            [6.3, 2.8, 5.1, 1.5, 0],
            [6.2, 2.8, 4.8, 1.8, 0],
            [6.7, 3.1, 4.4, 1.4, 2],
            [6.0, 2.7, 5.1, 1.6, 2],
            [6.5, 3.0, 5.5, 1.8, 0],
            [6.1, 3.0, 4.9, 1.8, 0],
            [5.6, 3.0, 4.1, 1.3, 2],
            [4.7, 3.2, 1.6, 0.2, 1],
            [6.6, 3.0, 4.4, 1.4, 2]]


def split_sets(start, finish):
    x, y = get_matrix_and_vector()
    return x[start:finish], y[start:finish]


def get_matrix_and_vector():
    data = get_dataset()
    X = [data_entry[:-1] for data_entry in data]
    y = [data_entry[-1] for data_entry in data]
    return X, y


if __name__ == '__main__':
    thirty_percent = int(0.3 * len(get_dataset()))

    tree_1 = DecisionTreeClassifier()
    x, y = split_sets(0, thirty_percent)
    tree_1.fit(x, y)

    tree_2 = DecisionTreeClassifier()
    x, y = split_sets(thirty_percent, 2 * thirty_percent)
    tree_2.fit(x, y)

    tree_3 = DecisionTreeClassifier()
    x, y = split_sets(2 * thirty_percent, len(get_dataset()))
    tree_3.fit(x, y)

    new_x = [[float(element) for element in input().split(',')][:-1]]

    prediction_1 = tree_1.predict(new_x)[0]
    prediction_2 = tree_2.predict(new_x)[0]
    prediction_3 = tree_3.predict(new_x)[0]

    votes = {
        0: 0,
        1: 0,
        2: 0
    }
    votes[prediction_1] += 1
    votes[prediction_2] += 1
    votes[prediction_3] += 1

    print(f'Glasovi: {votes}')
    pred = 'unknown'
    if votes[0] > votes[1] and votes[0] > votes[2]:
        pred = 0
    elif votes[1] > votes[0] and votes[1] > votes[2]:
        pred = 1
    elif votes[2] > votes[0] and votes[2] > votes[1]:
        pred = 2

    print(f'Predvidena klasa: {pred}')
