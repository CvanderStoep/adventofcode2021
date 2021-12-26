def read_input_file():
    # This is day3 part 1
    filename = "input3.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    number_of_ones = [0] * 12
    gamma = [0] * 12
    epsilon = [0] * 12

    for line in content:
        for i in range(12):
            number_of_ones[i] += int(line[i])
    for i in range(12):
        gamma[i] = round(number_of_ones[i] / len(content))
        epsilon[i] = abs(gamma[i] - 1)

    gamma = "".join(str(elem) for elem in gamma)
    epsilon = "".join(str(elem) for elem in epsilon)

    print(f'gamma rate (binary): {gamma}')
    gamma = int(gamma, 2)  # convert binary string to decimal integer
    print(f'gamma rate (decimal): {gamma}')

    print(f'epsilon rate (binary): {epsilon}')
    epsilon = int(epsilon, 2)
    print(f'epsilon rate (decimal): {epsilon}')

    print(f'power consumption = {gamma * epsilon}')


if __name__ == '__main__':
    read_input_file()
