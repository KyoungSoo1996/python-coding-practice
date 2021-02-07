# 다익스트라 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 
# 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 알려주는 알고리즘이다.
# 음의 간선이 없을 때 정상적으로 동작하며, 기본적으로 그리디 알고리즘으로 분류된다.

# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 3번과 4번을 반복한다.

import heapq
# import sys

# # 데이터 입력을 위한 것
# input = sys.stdin.readline
# # 무한을 의미하는 값으로 10억을 설정
# INF = int(1e9)

# # 노드의 개수, 간선의 개수
# n, m = map(int, input().split())
# # 시작 노드의 번호
# start = int(input())
# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
# graph = [[] for i in range(n+1)]
# # 최단 거리 테이블 초기화
# distance = [INF] * (n + 1)

# #모든 간선 입력받기
# for _ in range(m):
#     # a번 노드에서 b번 노드까지 c 비용이 든다.
#     a, b, c = map(int, input().split())
#     graph[a].append(b,c)

# def dijkstra(start):
#     q = []
#     # 시작 노드로 가기 위한 최단 경로는 0이며, 큐에 삽입한다.
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     # 큐에 데이터가 있다면
#     while q:
#         # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#         dist, now = heapq.heappush(q)
#         # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
#         if distance[now] < dist:
#             continue
#         # 현재 노드와 연결된 다른 인접한 노드들을 확인한다.
#         for i in graph[now]:
#             cost = dist + i[1]
#             # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost,i[0]))

# dijkstra(start)

# for i in range(1, n+1):
#     if distance[i] == INF:
#         print("INFINITY")
#     else:
#         print(distance[i])

start = 1
points = 6
links = [
    [1,2,2],
    [1,3,5],
    [1,4,1],
    [2,3,3],
    [2,4,2],
    [3,2,3],
    [3,6,5],
    [4,3,3],
    [4,5,1],
    [5,3,1],
    [5,6,2]
]

def Dijkstra(start, points, links):
    # 데이터 초기화 및 가져오기
    distances = [int(1e9)] * (points + 1)
    graph = [[] for i in range(points + 1)]
    for i in links:
        graph[i[0]].append((i[1],i[2]))
    #########################
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:            
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동할 때 거리가 더 짧은 경우
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distances

print(Dijkstra(start, points, links))
