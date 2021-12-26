def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = set()
    output_fold = []
    for line in content:
        # output_values.append(line)
        # output_values.append(list(map(int, list(line))))
        if ',' in line:
            x, y = line.split(',')
            output_values.add((int(x), int(y)))
        elif 'fold' in line:
            direction, value = line.split('=')
            output_fold.append([direction[-1], int(value)])

    return output_values, output_fold


def fold_paper(data, direction, value):
    new_data_set = set()
    for elem in data:
        x = elem[0]
        y = elem[1]
        if direction == 'y':
            if y < value:
                new_data_set.add((x, y))
            else:
                x_new = x
                y_new = 2 * value - y
                new_data_set.add((x_new, y_new))
        else:
            if x < value:
                new_data_set.add((x, y))
            else:
                x_new = 2 * value - x
                y_new = y
                new_data_set.add((x_new, y_new))

    return new_data_set


def pretty_print(data):
    (max_x, max_y) = (max([x for (x, _) in data]), max([y for (_, y) in data]))

    for j in range(0, max_y + 1):
        for i in range(0, max_x + 1):
            if (i, j) in data:
                print('#', end="")
            else:
                print(".", end="")
        print()
    print(data)


if __name__ == '__main__':
    # This is day 13
    filename = "input/input13test.txt"
    data, folds = read_input_file(filename)

    new_set = fold_paper(data, folds[0][0], folds[0][1])
    print(f'part 1: {len(new_set)} dots are visible')

    for fold in folds:
        data = fold_paper(data, fold[0], fold[1])
        print(f'part 2: output signal')
        pretty_print(data)
