def solution(arr):
    answer = []
    temp = -1
    for i in arr:
        if temp != i:
            temp = i
            answer.append(i)
    return answer


def best_solution(arr):
    return [arr[i] for i in range(len(arr)) if arr[i] != arr[i + 1 : i + 2]]


testarr = [0, 1, 3, 3, 0, 1, 1]

print(solution(testarr))
print(solution(testarr))
