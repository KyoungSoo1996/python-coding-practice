

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer


def best_solution(x, n):
    return [i*x + x for i in range(n)]


print(solution(2, 5))
print(best_solution(2, 5))
