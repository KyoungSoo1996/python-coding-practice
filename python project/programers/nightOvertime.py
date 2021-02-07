#효율성 실패
def solution(n, works):
    answer = 0
    #시간이 할일보다 많거나 같은지 계산
    if sum(works) <= n:
        return 0
    #할일 계산
    while n > 0 :
        maxTime = 0
        maxNum = 0
        for work in range(len(works)):
            if maxTime < works[work]:
                maxTime = works[work]
                maxNum = work
        works[maxNum] -= 1
        n -= 1
    #야근 지수 계산
    for work in works:
        answer += work**2
    return answer


testWorks = [4,3,3]
testN = 4
print(solution(testN, testWorks))
