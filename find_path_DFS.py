# Find all paths to between source to destination

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}


def find_path_DFS(graph,start,end,path=[]):
    path = path + [start]
    if start == end:
        return path

    paths = []
    for node in graph[start]:
        if node not in path:
            new_path = find_path_DFS(graph,node,end,path)

            if len(new_path) > 0:
                paths.extend(new_path)

    return paths

print(find_path_DFS(graph,'A','C'))

