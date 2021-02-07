#시간 초과
# def solution(N, stages):
#     answer = []

#     calcFauilure = [[0 for i in range(2)] for j in range(N)]
#     for i in range(1,N+1):
#         tempReach = 0
#         tempFauilure = 0
#         calcFauilure[i-1][0] = i
#         for player in stages:
#             if i <= int(player):
#                 tempReach += 1
#             if i == int(player):
#                 tempFauilure += 1
#         if tempReach == 0:
#             calcFauilure[i-1][1] = 0
#         else:
#             calcFauilure[i-1][1] = tempFauilure/tempReach
#     calcFauilure = sorted(calcFauilure, key = lambda x: (-x[1], x[0]))

#     for i in range(len(calcFauilure)):
#         answer.append(calcFauilure[i][0])

#     return answer

def solution(N, stages):
    dic = {}
    n = len(stages)
    for i in range(1,N+1):
        if stages.count(i) == 0 : 
            dic[i] = 0 
            continue
        item = stages.count(i)/n
        n-=stages.count(i)
        dic[i] = item
    return sorted(dic, key=lambda k : dic[k], reverse = True)

testN = 5
testStage = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(testN,testStage))
