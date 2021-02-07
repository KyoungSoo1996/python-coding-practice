#그래프 DFS 구현하기

graph = [
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
checked = [False] * 9

answer = []
def DFS(graph, checked, currentPos):
    answer.append(currentPos)
    if not checked[currentPos]:
        checked[currentPos] = True
        for i in graph[currentPos]:
            if not checked[i]:
                DFS(graph, checked, i)
    return answer
    

print(DFS(graph, checked, 1))

