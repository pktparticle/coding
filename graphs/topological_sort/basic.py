"""
Notes -
- only possible for directed acyclic graphs
- cyclic graphs will have cyclic dependencies which makes it impossible to have topological sort
- source: no incoming edge [in-degree = 0]
- sink: no outgoing edge [out-degree = 0]
- in-degree: count of incoming edges
- out-degree: count of outgoing edges
"""
from collections import deque
from typing import List, Tuple


def topological_sort(vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Approach
    - initialize the graph
    - build the graph
    - find all the sources
    - do sort
    """
    sorted_order = []
    inDegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        inDegree[v] += 1

    source = deque()
    for vertex in inDegree:
        if inDegree[vertex] == 0:
            source.append(vertex)

    while source:
        vertex = source.popleft()
        sorted_order.append(vertex)
        for node in graph[vertex]:
            inDegree[node] -= 1

            if inDegree[node] == 0:
                source.append(node)

    if len(sorted_order) == vertices:
        return sorted_order
    return []


print(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))

"""
Sample problems:
https://leetcode.com/problems/course-schedule/description/
https://leetcode.com/problems/course-schedule-ii/description/
"""