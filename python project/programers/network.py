# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
# 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

ex1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
ex2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
ex3 = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]


def DFS(x, y, n, computer):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if computer[x][y] == 1:
        computer[x][y] = 0
        DFS(x, y + 1, n, computer)
        DFS(x, y - 1, n, computer)
        DFS(x + 1, y, n, computer)
        DFS(x - 1, y, n, computer)
        return True
    return False


def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if DFS(i, j, n, computers):
                answer += 1
    return answer


print(solution(4, ex3))
