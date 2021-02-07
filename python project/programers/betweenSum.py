def solution(a: int, b: int) -> int:
    answer = 0
    if a == b:
        answer = a
    elif a > b:
        for num in range(b, a+1):
            answer += num
    else:
        for num in range(a, b+1):
            answer += num
    return answer


def best_solution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))


print(solution(2, 1))
print(best_solution(2,1))