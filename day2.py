def read_input_file():
    # This is day2 part 2
    filename = "input2.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    horizontal = 0
    vertical = 0
    aim = 0
    for line in content:
        command = line.split(' ')
        direction = command[0]
        amount = int(command[1])
        if direction == 'forward':
            horizontal += amount
            vertical += aim * amount
        elif direction == 'up':
            aim -= amount
        else: # down
            aim += amount
    print(f'vertical = {vertical}, horizontal = {horizontal}')
    print(f'multiplication = {horizontal * vertical}')


if __name__ == '__main__':
    read_input_file()
