graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': [],
    '9': ['10'],
    '10': []
}


def dfs(visited, graph, input_node, output_path=[]):  # function for dfs
    print(f'output_path = {output_path}')
    print(f'visted = {visited}')
    if input_node not in visited:
        output_path.append(input_node)
        visited.add(input_node)
        for neighbour in graph[input_node]:
            dfs(visited, graph, neighbour)
    return output_path


def find_connected_components(input_graph):
    visited = []
    connected_components = []
    for node in input_graph:
        if node not in visited:
            cc = []  # connected component
            dfs_traversal(input_graph, node, visited, cc)
            connected_components.append(cc)
    return connected_components


def dfs_traversal(input_graph, start, visited, path):
    if start in visited:
        return visited, path
    visited.append(start)
    path.append(start)
    for node in input_graph[start]:
        dfs_traversal(input_graph, node, visited, path)


# Driver Code
# visited = set()  # Set to keep track of visited nodes of graph.
# print("Following is the Depth-First Search")
# path = dfs(visited, graph, '5')
# print(path)


connected_components = find_connected_components(graph)
for cc in connected_components:
    print(cc)
