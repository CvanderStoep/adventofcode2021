""""
Data model:
position: tuple(A, (2,3))
board: list[positions]
state: tuple(energy, sorted(board))
priorityQueue: [states]
visited: set(str(boards))
"""

from queue import PriorityQueue

energy_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.readlines()
    return content


def calculate_initial_positions(data):
    total = 0
    positions = []
    y = 2
    for line in data:
        line = line.replace('\n', '')
        if 'A' in line or 'B' in line or 'C' in line:
            x = 3
            for c in line.split('#'):
                if c in ['A', 'B', 'C', 'D']:
                    positions.append((c, (x, y)))
                    x = x + 2
            y = y + 1
    return positions


def in_room_safely(type, position, positions):
    x = {'A': 3, 'B': 5, 'C': 7, 'D': 9}[type]
    if position[0] != x:
        return False
    if position[1] == 3:
        return True
    return positions[(x, 3)] == type


def all_room_moves(type):
    if type == 'A':
        return [(3, 2), (3, 3)]
    if type == 'B':
        return [(5, 2), (5, 3)]
    if type == 'C':
        return [(7, 2), (7, 3)]
    if type == 'D':
        return [(9, 2), (9, 3)]


def room_moves(type, positions):
    room = all_room_moves(type)
    if not room[1] in positions:
        return [room[1]]
    if positions[room[1]] == type:
        return [room[0]]
    return []


def hallway_moves():
    return [(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)]


def is_blocked(start, end, positions):
    for hallway in hallway_moves():
        if not hallway in positions:
            continue
        if (start[0] - hallway[0]) * (end[0] - hallway[0]) < 0:
            return True

    if start[1] == 3 and (start[0], 2) in positions:
        return True
    return end[1] == 3 and (end[0], 2) in positions


def cost(position, move):
    x = abs(position[1][0] - move[0])
    y = abs(position[1][1] - move[1])
    up = abs(position[1][1] - 1)
    down = abs(move[1] - 1)
    distance = x + up + down
    return distance * energy_costs[position[0]]


def moves(position, board):
    positions_dictionary = {x: y for (y, x) in board}
    if in_room_safely(position[0], position[1], positions_dictionary):
        return []
    all_moves = room_moves(position[0], positions_dictionary)
    if position[1][1] != 1:
        all_moves = all_moves + hallway_moves()

    all_moves = [
        x
        for x in all_moves
        if (not x in positions_dictionary) and
           not is_blocked(position[1], x, positions_dictionary)
    ]
    return all_moves


def is_done(positions):
    a = 0
    b = 0
    c = 0
    d = 0
    for position in positions:
        if position[0] == 'A' and position[1][0] == 3:
            a = a + 1
        if position[0] == 'B' and position[1][0] == 5:
            b = b + 1
        if position[0] == 'C' and position[1][0] == 7:
            c = c + 1
        if position[0] == 'D' and position[1][0] == 9:
            d = d + 1
    return a == 2 and b == 2 and c == 2 and d == 2


def add_states_to_queue(board, base_energy, queue):
    for position in board:
        _moves = moves(position, board)
        for _move in _moves:
            energy = base_energy + cost(position, _move)
            new_state = [x for x in board if x[1] != position[1]]
            new_state.append((position[0], _move))
            queue.put((energy, sorted(new_state)))


def next_state(queue, visited):
    #  puzzle_status = 0  # 0: no solution, -1: visited before, other: done

    state = queue.get()
    base_energy = state[0]
    board = state[1]
    if str(board) in visited:
        return -1
    visited.add(str(board))
    if is_done(board):
        return base_energy
    add_states_to_queue(board, base_energy, queue)

    return 0


def solve_puzzle(data):
    positions = calculate_initial_positions(data)
    visited = set()
    queue = PriorityQueue()
    queue.put((0, sorted(positions)))

    while not queue.empty():
        mode = next_state(queue, visited)
        if mode == -1:  # state visited before
            continue
        elif mode != 0:  # solution found
            total = mode
            break
    print("Answer: " + str(total))


if __name__ == '__main__':
    # This is day 23 with a little bit of help from Google : - )
    filename = "input/input23b.txt"
    data = read_input_file(filename)
    solve_puzzle(data)
