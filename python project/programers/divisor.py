#n의 약수를 더해라
def solution(n: int) -> int:
    answer = 0
    for count in range(1, n+1):
        if n % count == 0:
            answer += count
    return answer


print(solution(10))
