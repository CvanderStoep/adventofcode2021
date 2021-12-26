import matplotlib.pyplot as plt
import networkx as nx

from day9c import surrounding


def read_input_file(input_file):
    with open(input_file) as f:
        content = f.read().splitlines()

    output_values = []
    for line in content:
        output_values.append(list(map(int, list(line))))
    return output_values


def define_graph(input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    DG = nx.DiGraph()
    for i in range(rows):
        for j in range(cols):
            for x, y in surrounding(input_data, i, j):
                DG.add_edge((i, j), (x, y), weight=input_data[x][y])
    return DG


def path_pretty_print(path, input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    for i in range(rows):
        for j in range(cols):
            if (i, j) in path:
                print(input_data[i][j], end="")
            else:
                print('0', end="")
        print()


def calculate_total_risk(path, input_data):
    total_risk = -input_data[0][0]  # cel (0,0) does not count
    for cel in path:
        total_risk += input_data[cel[0]][cel[1]]
    print(f'total risk= {total_risk}')


def five_data(input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    for i in range(rows):
        for j in range(cols, cols * 5):
            risk = (input_data[i][j - cols] + 1)
            if risk == 10:
                risk = 1
            input_data[i].append(risk)

    for i in range(rows * 4):
        risk_list = []
        for risk in input_data[i]:
            risk += 1
            if risk == 10:
                risk = 1
            risk_list.append(risk)
        input_data.append(risk_list)

    return input_data


if __name__ == '__main__':
    # This is day 15 part1 and part2
    filename = "input/input15.txt"
    data = read_input_file(filename)
    data = five_data(data) # this is part 2; comment to find solution for part 1
    DG = define_graph(data)

    target_cel = (len(data) - 1, len(data[0]) - 1)
    shortest_path = nx.shortest_path(DG, source=(0, 0), target=target_cel, weight='weight')
    path_pretty_print(shortest_path, data)
    calculate_total_risk(shortest_path, data)

    # pos = nx.spring_layout(DG)
    # nx.draw(DG, with_labels=True, pos=pos)
    # plt.show()
    # print(nx.to_dict_of_dicts(DG))
