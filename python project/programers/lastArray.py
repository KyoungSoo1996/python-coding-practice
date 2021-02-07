def solution(s: str):
    answer = ''
    for i in range(len(s)):
        answer += answer.join(s[-i - 1])
    return answer


print(solution('1234567890'))
