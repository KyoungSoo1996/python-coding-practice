point = 4
line = 5
startPoint = 1
pointLink = [
    [1,2],
    [1,3],
    [1,4],
    [2,4],
    [3,4]
]

def MakeGraph(point, pointLink):
    graph = [[] * 1 for i in range(point+1)]
    for i in range(0, point):
        
        for j in range(len(pointLink)):
            if i == pointLink[j][0]:
                graph[i].append(pointLink[j][1])
    return graph

def DFS(graph, pos, visitPos, answer):
    visitPos[pos] = True
    for i in graph[pos]:        
        if not visitPos[i]:            
            answer.append(i)
            DFS(graph, i, visitPos, answer)

def DFSGraph(start, point, pointLink):
    answer = [start]
    graph = MakeGraph(point, pointLink)
    visitPos = [False] * (point + 1)
    DFS(graph, start, visitPos, answer)
    return answer

print(DFSGraph(startPoint, point, pointLink))