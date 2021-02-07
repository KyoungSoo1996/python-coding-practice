def solution(n):
    answer = []
    for i in range(len(str(n))):
        answer.append(int(str(n)[len(str(n)) - i-1]))
    return answer

def best_solution(n):
    return list(map(int, reversed(str(n))))


print(solution(12345))
print(best_solution(12345))