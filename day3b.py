def read_input_file():
    # This is day3 part 2
    filename = "input3.txt"
    with open(filename) as f:
        content = f.read().splitlines()
    oxygen_rating = []
    co2_scrubber_rating = []

    for line in content:
        oxygen_rating.append(line)
        co2_scrubber_rating.append(line)

    digit = 0
    while len(oxygen_rating) > 1:
        number_of_ones = 0
        for line in oxygen_rating:
            number_of_ones += int(line[digit])
        # gamma_digit = most common digit; round 0.5 towards 1 in case of a draw
        gamma_digit = round(number_of_ones / len(oxygen_rating) + 0.000001)
        oxygen_rating = [elem for elem in oxygen_rating if int(elem[digit]) == gamma_digit]
        digit += 1

    digit = 0
    while len(co2_scrubber_rating) > 1:
        number_of_ones = 0
        for line in co2_scrubber_rating:
            number_of_ones += int(line[digit])
        gamma_digit = round(number_of_ones / len(co2_scrubber_rating) + 0.000001)
        # epsilon_digit = least common digit
        epsilon_digit = abs(gamma_digit - 1)
        co2_scrubber_rating = [elem for elem in co2_scrubber_rating if int(elem[digit]) == epsilon_digit]
        digit += 1

    oxygen_rating = "".join(str(elem) for elem in oxygen_rating[0])
    co2_scrubber_rating = "".join(str(elem) for elem in co2_scrubber_rating[0])

    print(f'oxygen generator rating (binary): {oxygen_rating}')
    oxygen_rating = int(oxygen_rating, 2)
    print(f'oxygen generator rating (decimal): {oxygen_rating}')

    print(f'CO2 scrubber rating (binary): {co2_scrubber_rating}')
    co2_scrubber_rating = int(co2_scrubber_rating, 2)
    print(f'CO2 rating (decimal): {co2_scrubber_rating}')

    print(f'life support rating = {oxygen_rating * co2_scrubber_rating}')


if __name__ == '__main__':
    read_input_file()
