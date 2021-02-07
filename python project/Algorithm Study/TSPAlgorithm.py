#TSP(Travelling Salesman Problem) : 여행하는 외판원 문제
#이 문제는 조합 최적화 문제로 전산학에서 연구된 가장 유명한 문제다
#INPUT : 도시의 개수, 도시간 거리
#OUTPUT : 모든 도시를 한 번씩 방문하고 처음으로 돌아올 수 있는 최단거리 경로

#Fuction modeling
#find_path(start, last, V, tmp_dist):
#   여행을 start에서 시작한다.
#   현재까지 방문한 중간 경로의 마지막 도시는 last이다.
#   방문한 도시의 집합은 V이다.
#   중간 경로의 길이는 tmp_dist 이ㅏㄷ.
#   이때 중간 경로를 사용해서 경로를 마쳤을 때의 최소값을 구하라

#Pseudo code Modeling
# ans = infinite
# 
# find_path(start, last, V, tmp_dist):
#   if 모든 도시를 방문했다면:
#       return_home_dist = D[last][start] or infinite
#       ans = min(ans, tmp_dist + return_home_dist)
#       return
# 
#   for left_city in V^c:
#       if last와 left_city가 연결되어 있다면:
#           left_city를 방문 및 V에 추가
#           find_path(start, left_city,)
#           V에서 left_city를 제거.

def tsp(D):
    N = len(D)
    inf = float('inf')
    ans = inf
    VISITED_ALL = (1 << N) -1

    def find_path(start, last, visited, tmp_dist):
        nonlocal ans
        if visited == VISITED_ALL:
            return_home_dist = D[last][start] or inf
            ans = min(ans, tmp_dist + return_home_dist)
            return
        
        for city in range(N):
            if visited & (1 << city) == 0 and D[last][city] != 0:
                find_path(start, city, visited | (1 << city), tmp_dist + D[last][city])
        
    for c in range(N):
        find_path(c, c, 1<< c, 0)

    return ans

print(tsp(10))