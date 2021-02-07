def solution(n: int) -> str:
    answer = ''
    for count in range(n):
        if count % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer


def best_solution(n):
    return ("수박" * n)[0:n]


print(solution(3))
print(best_solution(3))
