def solution(n):
    answer = 0
    group = sorted(list(str(n)), reverse = True)
    for i in range(len(group)):
        answer += 10**(len(group) - i - 1)*int(group[i])
    return answer

def best_solution(n):
    ls = list(str(n))
    ls.sort(reverse= True)
    return int("".join(ls))

def best_mysolution(n):
    return int(''.join(sorted(list(str(n)), reverse = True)))

print(solution(23482))
print(best_solution(23482))
print(best_mysolution(23482))