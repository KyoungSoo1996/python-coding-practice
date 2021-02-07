def divisor(n):
    answer = []
    for i in range(1, n+1):
        if(n % i == 0):
            answer.append(i)
    return answer


def solution(n, m):
    answer = []
    one = divisor(n)
    two = divisor(m)
    temp = 1
    for i in one:
        for j in two:
            if i == j and temp < i:
                temp = i
    answer.append(temp)
    if(temp == 1):
        answer.append(n*m)
    else:
        answer.append(int(answer[0] * m/answer[0] * n/answer[0]))
    return answer


def best_solution(n, m):
    c, d = max(n, m), min(n, m)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n*m/c)]

    return answer


print(solution(2, 5))
print(best_solution(2,5))