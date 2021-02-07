# 어떤 나라에는 N개의 도시가 있다.
# 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내 메시지를 전송한다.
# 하지만 각 도시로 보내고자 하려면, 통로가 설치되어 있어야한다.
# 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

# 어느 날 C라는 도시에서 위급 상황이 발생했다.
# 최대한 많은 도시로 메시지를 보내고자 하는데,
# 이때 메시지를 받게 되는 도시의 개수와 도시들이 모두 메시지를 받는 데 걸리는 시간을 계산하시오.

# 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
# 둘째 줄부터 M+1 번째 줄에 걸쳐서 통로에 대한 정보가 주어진다.(시작, 도착, 거리)

cityCount = 3
linkCount = 2
startCity = 1
links = [[1, 2, 4], [1, 3, 2]]


def floyid(cityCount, startCity, links):
    INF = int(1e9)
    graph = [[INF] * (cityCount + 1) for i in range(cityCount + 1)]

    # 같은 정점에서는 거리가 0이다
    for i in range(0, cityCount + 1):
        graph[i][i] = 0

    # 링크에 기록되어 있는 정점 정보 저장
    for link in links:
        graph[link[0]][link[1]] = link[2]
        graph[link[1]][link[0]] = link[2]

    #플로이드 워셜 알고리즘 사용
    for a in range(0, cityCount + 1):
        for b in range(0, cityCount + 1):
            for c in range(0, cityCount + 1):
                graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

    graph = graph[1:]
    for i in graph:
        i.pop(0)

    count = 0
    distList = []
    # 전달된 도시 수
    for city in graph[startCity - 1]:
        if city not in (0, INF):
            count += 1
            distList.append(city)
    # 최대 거리

    return (count, max(distList))


print(floyid(cityCount, startCity, links))
