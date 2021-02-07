# n은 지점의 개수
# s는 시작점
# a는 a의 도착점
# b는 b의 도착점
# fares는 [시작, 끝, 요금]

n = 6
s = 4
a = 6
b = 2

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50],
         [2, 4, 66], [2, 3, 22], [1, 6, 25]]


def printGrapy(grapy):
    for i in grapy:
        print(i)


# import heapq

# def solution(n, s, a, b, fares):
#     INF = int(1e9)
#     distance = [INF] * (n + 1)
#     grapy = [[] for i in range(n + 1)]
#     for i in fares:
#         grapy[i[0]].append((i[1], i[2]))
#         grapy[i[1]].append((i[0], i[2]))
#     road = []
#     distance, grapy, road = dijkstra(s, distance, grapy)
#     print(road)
#     print(a)
#     print(b)
#     return distance

# def dijkstra(start, distance, grapy):
#     q = []
#     road = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         road.append(now)
#         if distance[now] < dist:
#             continue
#         for i in grapy[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#     return distance, grapy, road


def solution(n, s, a, b, fares):
    INF = int(1e9)
    grapy = [[INF] * (n + 1) for i in range(n + 1)]
    for i in range(n + 1):
        grapy[i][i] = 0

    for i in fares:
        grapy[i[0]][i[1]] = i[2]
        grapy[i[1]][i[0]] = i[2]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                grapy[i][j] = min(grapy[i][j], grapy[i][k] + grapy[k][j])

    temp = []
    for wow in range(1, n + 1):
        temp.append(grapy[s][wow] + grapy[wow][a] + grapy[wow][b])
    return min(grapy[s][a] + grapy[a][b], grapy[s][a] + grapy[s][b],
               grapy[s][b] + grapy[b][a], min(temp))


print(solution(n, s, a, b, fares))
