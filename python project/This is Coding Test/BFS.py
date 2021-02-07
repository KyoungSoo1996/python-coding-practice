from collections import deque

grapy = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

def BFS(grapy, current, visited):
    result = [1]
    queue = deque([current])
    visited[current] = True
    while queue:
        current = queue.popleft()
        for i in grapy[current]:
            if not visited[i]:
                result.append(i)
                queue.append(i)
                visited[i] = True
    return result
print(BFS(grapy, 1, visited))