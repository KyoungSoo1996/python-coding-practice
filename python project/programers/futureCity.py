# 방문 판매원 A는 많은 회사가 모여 있는 공중 미래 도시에 있다.
# 공중 미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
# 방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.

# 공중 미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.
# 또한 연결된 2개의 회사는 양방향으로 이동할 수 있다.
# 공중 미래 도시에서의 도로는 마하의 속도로 사람을 이동시켜주기 때문에 특정 회사와 다른 회사가 도로로 연결되어 있다면 1만큼의 시간이 걸린다.
# 또한 오늘 방문 판매원 A는 기대하던 소개팅에도 참석하고자 한다.
# 소개팅의 상대는 K번 회사에 존재한다.
# 이때 방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

# 첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어진다.
# 둘째 줄부터 M+1 번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 있다.
# M+2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다.

#플로이드 워셜 알고리즘
# INF = int(1e9)

# points = 4
# links = 7
# graphMap = [[1, 2, 4], [1, 4, 6], [2, 1, 3], [2, 3, 7], [3, 1, 5], [3, 4, 4],
#             [4, 3, 2]]

# def Floyd(points, links, graphMap):
#     # 전체 경로 10억으로 초기화
#     graph = [[INF] * (points + 1) for i in range(points + 1)]

#     # 자기 자신 노드까지 가는 거리 = 0
#     for i in range(1, points + 1):
#         for j in range(1, points + 1):
#             if i == j:
#                 graph[i][j] = 0

#     # 간선에 대한 정보 입력하기
#     for i in graphMap:
#         graph[i[0]][i[1]] = i[2]
#     print(graph)

#     for a in range(1, points + 1):
#         for b in range(1, points + 1):
#             for c in range(1, points + 1):
#                 graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

#     return graph[1:]

# print(Floyd(points, links, graphMap))

totalWorkspace = 4
totalLink = 2
links = [[1, 3], [2, 4]]
startWorkspace = 1
targetWorkspace = 3
subtargetWorkspace = 4
INF = int(1e9)


def cityVisit(totalWorkspace, links, startWorkspace, targetWorkspace,
              subtargetWorkspace):
    distances = [[INF] * (totalWorkspace + 1)
                 for i in range((totalWorkspace + 1))]

    # 같은 정점일 경우에 경로가 0이다.
    for i in range(totalWorkspace + 1):
        for j in range(totalWorkspace + 1):
            if i == j:
                distances[i][j] = 0

    # 링크에 저장되어 있는 노드는 거리가 전부 1이다.
    for link in links:
        distances[link[0]][link[1]] = 1
        distances[link[1]][link[0]] = 1

    # 플로이드 워셜 알고리즘 사용
    for a in range(totalWorkspace + 1):
        for b in range(totalWorkspace + 1):
            for c in range(totalWorkspace + 1):
                distances[b][c] = min(distances[b][c],
                                      distances[a][c] + distances[b][a])
    result = 0
    result = distances[startWorkspace][subtargetWorkspace] + distances[
        subtargetWorkspace][targetWorkspace]

    if result >= 1000000000:
        return -1
    else:
        return result


print(
    cityVisit(totalWorkspace, links, startWorkspace, targetWorkspace,
              subtargetWorkspace))
