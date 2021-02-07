def DFS(cnt, target, numList):
    if cnt == target:
        return True
    elif cnt > target:
        return False
    else:
        DFS()


def solution(numbers, target):
    answer = 0
    return answer


print(solution([1, 1, 1, 1, 1], 3))