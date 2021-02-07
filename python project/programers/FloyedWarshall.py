#다익스트라 알고리즘 구현하기

#인자값 start, graph, point
import heapq

pointCount = 6
startPoint = 1
# start/end/distance
links = [[1, 2, 2], [1, 3, 5], [1, 4, 1], [2, 3, 3], [2, 4, 2], [3, 2, 3],
         [3, 6, 5], [4, 3, 3], [4, 5, 1], [5, 3, 1], [5, 6, 2]]


def Dijkstra(start, links, points):
    # 거리를 담을 배열 하나 선언(최소를 구해야 하므로 10억을 넣는다.)
    distance = [int(1e9)] * (points + 1)
    #links에 있는 데이터 정제해서 연산하기 쉬운 형태로 수정하기
    graph = [[] for i in range(points + 1)]
    for i in links:
        graph[i[0]].append((i[1], i[2]))

    # 시작 정점의 거리를 0으로 추가한다.
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, point = heapq.heappop(q)
        if dist > distance[point]:
            continue
        for i in graph[point]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[1:]


print(Dijkstra(startPoint, links, pointCount))

# 다익스트라 알고리즘은 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우에 사용할 수 있는 최단 경로 알고리즘이다.
# 이번에 설명하는 플로이드 워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용할 수 있는 알고리즘이다.

# 다익스트라 알고리즘은 단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택한다.
# 그리고 해당 노드를 거쳐 가는 경로를 확인하며, 최단 거리 테이블을 갱신하는 방식으로 동작한다.
# 플로이드 워셜 알고리즘 또한 단계마다 거쳐 가는 노드를 기준으로 알고리즘을 수행한다.
# 하지만 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다는 점이 다르다.

# 플로이드 워셜 알고리즘은 다익스트라 알고리즘과는 다르게 2차원 리스트에 최단 거리 정보를 저장한다.
# 모든 노드에 대하여 다른 모든 노드로 가는 최단 거리 정보를 담아야 하기 때문이다.
# 때문에 N번의 단계에서 매번 N^2의 시간이 소요된다.

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)
