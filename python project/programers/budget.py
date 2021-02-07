def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d:
        if i <= budget:
            budget -= i
            answer += 1
    return answer

testD = [1,3,2,5,4]
testBudget = 9

print(solution(testD, testBudget))