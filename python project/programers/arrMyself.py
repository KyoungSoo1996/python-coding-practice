def solution(strings, n):
    answer = []
    hi = []
    temp = [[0 for col in range(2)] for row in range(len(strings))]
    for i in range(len(strings)):
        temp[i][0] = strings[i]
        temp[i][1] = ord(strings[i][n])
    hi = sorted(temp, key=lambda x: (x[1], x[0]))
    print(hi)
    for i in range (len(strings)):
        answer.append(hi[i][0])
    return answer

def best_solution(strings, n):
    return sorted(strings, key=lambda x: x[n])

teststrings = ['abcd','abce','cdx']
teststrings2 = ['sun', 'bed','car']
testn = 1
print(solution(teststrings, 2))
print(best_solution(teststrings, 2))