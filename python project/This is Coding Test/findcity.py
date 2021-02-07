# 1~N번까지의 도시에 M개의 단방향 도로가 있다.
# 모든 도로의 거리는 1이다.
# 이때 특정 도시인 X로 부터 출발하여 도달할 수 있는 도시 중 최단 거리가 K인 모든 도시의 번호를 출력하시오.

# 입력 -> 도시의 개수 : N, 도로의 개수 : M, 특정 거리 정보 : K, 출발 도시 : X, 특정 거리에 있는 도시가 없다면 -1

links = [
    [1,2],
    [1,3],
    [2,3],
    [2,4]
]
startCity = 1
citys = 4
dist = 2

def PrintMap(m):
    for i in m:
        print(i)

def FindCity(links, startCity, citys, dist):
    result = []
    INF = -1
    cityMap = [[INF] * (citys + 1) for i in range(citys + 1)]
    #map Making - self
    for i in range(citys+1):
        cityMap[i][i] = 0

    for i in links:
        cityMap[i[0]][i[1]] = 1
    
    PrintMap(cityMap)


    return result

# def DFS(x,y,citys, cityMap):



print(FindCity(links, startCity, citys, dist))
