import time
import heapq

"""
source code location:
https://github.com/Thespyinthehole/AdventOfCode2021/blob/master/Day23/puzzle1.py
"""

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


def in_room_safely(type, position, positions):
    x = {'A': 3, 'B': 5, 'C': 7, 'D': 9}[type]
    if position[0] != x:
        return False
    if position[1] == 3:
        return True
    return positions[(x, 3)] == type


def moves(pod, pods):
    positions = {x: y for (y, x) in pods}
    if in_room_safely(pod[0], pod[1], positions):
        return []
    all_moves = room_moves(pod[0], positions)
    if pod[1][1] != 1:
        all_moves = all_moves + hallway_moves()

    all_moves = [
        x
        for x in all_moves
        if (not x in positions) and
           not is_blocked(pod[1], x, positions)
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


energy_costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def cost(position, move):
    x = abs(position[1][0] - move[0])
    y = abs(position[1][1] - move[1])
    up = abs(position[1][1] - 1)
    down = abs(move[1] - 1)
    distance = x + up + down
    distance2 = x + y
    if distance != distance2:
        pass
    return distance * energy_costs[position[0]]


def add_states(board, base_energy, queue):
    for position in board:
        _moves = moves(position, board)
        for _move in _moves:
            energy = base_energy + cost(position, _move)
            new_state = [x for x in board if x[1] != position[1]]
            new_state.append((position[0], _move))
            heapq.heappush(queue, (energy, sorted(new_state)))


def next_state(queue, done):
    state = heapq.heappop(queue)
    base_energy = state[0]
    board = state[1]
    if str(board) in done:
        return -1
    done.add(str(board))
    if is_done(board):
        return base_energy
    add_states(board, base_energy, queue)
    return 0


def puzzle(data):
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

    done = set()
    queue = []
    heapq.heappush(queue, (0, positions))

    while len(queue) != 0:
        mode = next_state(queue, done)
        if mode == -1:
            continue
        elif mode != 0:
            total = mode
            break
    print("Answer: " + str(total))


# data = open(__file__.replace('.py', 'input'))
data = open("input/input23b.txt")
start = time.perf_counter()
puzzle(data.readlines())
end = time.perf_counter()
print("Time: ", end="")
time_taken = end - start
if time_taken * 1000 < 1:
    print(time_taken * 1000000, end="")
    print("ns")
else:
    print(time_taken * 1000, end="")
    print("ms")