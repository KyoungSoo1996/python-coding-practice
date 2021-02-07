def solution(budgets, M):
    print(sum(budgets))
    avgM = M//len(budgets)
    lostM = []
    for i in budgets:
        if i < avgM:
            lostM.append(avgM - i)
    return avgM + sum(lostM)//len(lostM)


testBudget = [120, 110, 140, 150]
testM = 485
print(solution(testBudget, testM))