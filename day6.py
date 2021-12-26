def read_input_file():
    # This is day6 part 1

    # for part 2, we will use a dictionay iso a list and only count the number of fish with a certain age.
    # dict{0:3, 1:4, etc}
    filename = "input6test.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    for line in content:
        initial_state = line.split(',')
    initial_state = list(map(int, initial_state))

    number_of_days = 256
    for i in range(number_of_days):
        print(f'after {i} days: ')
        number_of_zeros = initial_state.count(0)
        # new_fish = [8] * number_of_zeros
        initial_state = [elem - 1 if elem != 0 else 6 for elem in initial_state]
        for f in range(number_of_zeros):
            initial_state.append(8)

    # print(f'after {number_of_days} days: {initial_state}')
    print(f'number of fish after {number_of_days} days: {len(initial_state)}')


if __name__ == '__main__':
    read_input_file()
