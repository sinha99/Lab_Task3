# DFS algorithm
def traversal(adj_list, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for next_node in adj_list[start] - visited:
        if next_node not in visited:
            traversal(adj_list, next_node, visited)
    return visited


def dfs (graph,node):
    visited = [node]
    stack = [node]
    while stack:
        node = stack[-1]
        if node not in visited:
            visited.extend(node)
        remove_from_stack = True
        for next in graph(node):
            if next not in visited:
                stack.extend(next)
                remove_from_stack = False
                break
        if remove_from_stack:
            stack.pop()
    return visited






