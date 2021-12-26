def read_input_file():
    # This is day6 part 2

    # for part 2, we will use a dictionary iso a list and only count the number of fish with a certain age.
    # dict{0:3, 1:4, etc}
    filename = "input6.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    initial_state = []
    initial_state_dict = {}

    for i in range(9):
        initial_state_dict[i] = 0

    for line in content:
        initial_state = line.split(',')
    initial_state = list(map(int, initial_state))

    for elem in initial_state:
        initial_state_dict[elem] += 1

    number_of_days = 256
    for i in range(number_of_days):
        # print(f'after {i} days: ', initial_state_dict)

        old_zero_value = initial_state_dict[0]
        for j in range(6):
            initial_state_dict[j] = initial_state_dict[j+1]

        initial_state_dict[6] = old_zero_value + initial_state_dict[7]
        initial_state_dict[7] = initial_state_dict[8]
        initial_state_dict[8] = old_zero_value

    total_fish = 0
    for x in initial_state_dict.values():
        total_fish += x

    print(f'after {number_of_days} days: {initial_state_dict}')
    print(f'number of fish after {number_of_days} days: {total_fish}')


if __name__ == '__main__':
    read_input_file()
