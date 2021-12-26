def read_input_file():
    filename = "input1.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    depths = []
    for line in content:
        depths.append(int(line))

    number_of_increased_values = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            number_of_increased_values += 1

    print('measurements larger than previous:', number_of_increased_values)

    sum_depths = []
    for i in range(0, len(depths) - 2):
        sum_depths.append(depths[i] + depths[i + 1] + depths[i + 2])

    number_of_sum_increased_values = 0
    for i in range(1, len(sum_depths)):
        if sum_depths[i] > sum_depths[i - 1]:
            number_of_sum_increased_values += 1

    print('measurements larger than previous sum:', number_of_sum_increased_values)


if __name__ == '__main__':
    read_input_file()
