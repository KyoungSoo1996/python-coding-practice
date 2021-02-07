def solution(s: str):
    answer = ''
    temp = []
    for i in range(len(s)):
        temp.append(ord(s[i]))
    for j in range(len(temp)):
        answer += chr(sorted(temp, reverse=True)[j])
    return answer


def best_solution(s):
    return ''.join(sorted(s, reverse=True))


print(solution('Zbcdefg'))
print(best_solution('Zbcdefg'))