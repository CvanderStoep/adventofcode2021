from itertools import permutations


def read_input_file():
    # This is day8 part b

    listA = list('abcdefg')
    list_numbers = [0, 1, 2, 3, 4, 5, 6]

    digits_dict = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg',
                   6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}
    print(f'original dict: {digits_dict}')

    filename = "input8test.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    total_sum = 0
    for line in content:
        scrambled_digits = line.split('|')[0]
        scrambled_digits = scrambled_digits.split()

        list_numbers_perm = permutations(list_numbers)
        for perm in list_numbers_perm:
            scrambled_dict = {}
            for digit in range(10):
                check_original = digits_dict[digit]
                check_scrambled = ''
                for number in range(len(check_original)):
                    index_number = listA.index(check_original[number])
                    check_scrambled += listA[perm[index_number]]
                scrambled_dict[digit] = ''.join(sorted(check_scrambled))

            correct_permutation = True
            for scrambled_digit in scrambled_digits:
                sd = ''.join(sorted(scrambled_digit))
                if sd not in scrambled_dict.values():
                    correct_permutation = False

            if correct_permutation:  # found correct permutation, time to stop
                break

        scrambled_digits = line.split('|')[1]
        scrambled_digits = scrambled_digits.split()

        entry_output = ''
        for scrambled_digit in scrambled_digits:
            sd = ''.join(sorted(scrambled_digit))
            for key, value in scrambled_dict.items():
                if value == sd:
                    entry_output += str(key)
                    break
        print(f'entry output: {entry_output}')
        total_sum += int(entry_output)

    print(f'total sum= {total_sum}')


if __name__ == '__main__':
    read_input_file()
