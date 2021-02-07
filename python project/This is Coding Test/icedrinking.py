# N X M 크기의 얼음 틀이 있다.
# 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시한다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N,M <= 1,000)
# 두 번째 줄부터 N + 1번쨰 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

#ICE MAP
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

# iceMap = []
# N, M = map(int, input().split())
# for i in range(0, N):
#     iceMap.append(list(input().split()))

# def IceDrinkingSearching(x, y):
#     result = 0
#     if x < 0 or x >= N or y < 0 or y >= M:
#         return False
#     if iceMap[x][y] == '0':
#         iceMap[x][y] = '1'
#         IceDrinkingSearching(x,y+1)
#         IceDrinkingSearching(x,y-1)
#         IceDrinkingSearching(x+1,y)
#         IceDrinkingSearching(x-1,y)
#         return True
#     return False

# result = 0
# for i in range(N):
#     for j in range(M):
#         if IceDrinkingSearching(i,j) == True:
#             result += 1

# print(result)



#ICE MAP
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

graph = []

N, M = map(int, input().split())
for i in range(N):
    graph.append(list(input().split()))

def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if graph[x][y] == '0':
        graph[x][y] = '1'
        DFS(x, y+1)
        DFS(x, y-1)
        DFS(x-1, y)
        DFS(x+1, y)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if DFS(i,j) == True:
            result += 1

print(result)

