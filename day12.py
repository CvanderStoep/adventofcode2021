from collections import deque


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        elem = line.split('-')
        output_values.append(elem)

    return output_values


def create_cave_graph(input_data=[]):
    output_graph = {}
    for line in input_data:
        first = line[0]
        second = line[1]
        if first in output_graph:
            output_graph[first] += [second]
        else:
            output_graph[first] = [second]
        # create a bidirectional graph
        if second in output_graph:
            output_graph[second] += [first]
        else:
            output_graph[second] = [first]
    return output_graph


def find_path1(graph):
    starting_path = ['start']
    queue = deque([starting_path])
    all_possible_paths = []

    while queue:
        current_path = queue.pop()
        last_node = current_path[-1]
        if last_node == 'end':
            all_possible_paths.append(current_path)
            continue
        for neighbour in graph.get(last_node):
            is_valid_path_part1 = neighbour not in current_path or neighbour[0].isupper()
            if is_valid_path_part1:
                queue.append(current_path + [neighbour])
    return all_possible_paths


def find_path2(graph):
    starting_path = ['start']
    queue = deque([starting_path])
    all_possible_paths = []

    while queue:
        current_path = queue.pop()
        last_node = current_path[-1]
        if last_node == 'end':
            all_possible_paths.append(current_path)
            continue
        for neighbour in graph.get(last_node):
            if is_valid_path_part2(current_path ):
                queue.append(current_path + [neighbour])
    return all_possible_paths


def is_valid_path_part2(path):
    # maximum one double lowercase cave
    lower_case_path = [x for x in path if x.islower()]
    duplicate_item = [x for i, x in enumerate(lower_case_path) if x in lower_case_path[:i]]
    valid_path = True
    if len(duplicate_item) > 1:
        valid_path = False
    count_start = lower_case_path.count('start')
    count_end = lower_case_path.count('end')
    if count_start > 1 or count_end > 1:
        valid_path = False
    return valid_path


if __name__ == '__main__':
    # This is day 12 part1 & 2
    filename = "input/input12small.txt"
    data = read_input_file(filename)
    graph = create_cave_graph(data)

    path1 = find_path1(graph)
    path2 = find_path2(graph)

    print(f'input data= {graph}')
    for p in path2:
        print(f'path= {p}')
    print(f'part1: number of path= {len(path1)}')
    print(f'part2: number of path= {len(path2)}')
