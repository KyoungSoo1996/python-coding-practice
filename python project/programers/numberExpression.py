# 정수론 정리 : 표현할 수 있는 가짓 수 = 홀수 약수의 갯수
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 == 1:
            answer += 1
    return answer


print(solution(15))
