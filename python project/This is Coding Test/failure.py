# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1이상 N + 1 이하의 자연수가 담겨있다.
#  - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
#  - 단, N + 1은 마지막 스테이지까지 클리어한 사용자를 나타낸다.

# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수

N = 4
stages = [4,4,4,4,4,4]

def failure(N, stages):
    result = []
    failureStage = [0] * N
    for i in range(1,len(failureStage)+1):
        enter = 0
        noEnter = 0
        for j in stages:
            if j >= i:
                enter += 1
            if j == i:
                noEnter +=1
        result.append([i,noEnter/enter])
    answer = []
    for i in sorted(result, key= lambda x: -x[1]):
        answer.append(i[0])
    return answer

print(failure(N, stages))