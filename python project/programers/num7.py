# 왼쪽 숫자는 직원버호, 오른쪽 숫자는 매출액
# 직원번호 1번은 CEO이며, 팀장은 화살표를 받는 쪽이 될 수 없다.
# CEO를 제외한 나머지는 다른 누군가로부터 정확히 1개의 화살표를 받는다.

# 한 직원은 최대 2개의 팀에 속할 수 있다.
# 어떤 직원이 두 개의 팀에 속해있으면 하나의 팀에서는 팀장, 나머지 팀에서는 팀원

# 모든 팀은 최소 1명 이상의 직원을 워크숍에 참석시켜야함
# 회사의 매출액이 최소가 되어야함

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3],
         [10, 2]]


def solution(sales, links):
    answer = 0
    leader = []
    team = []

    grapy = [[] for _ in range(len(sales) + 1)]
    for i in links:
        grapy[i[0]].append((i[1], sales[i[1] - 1]))

    for i in grapy:
        if len(i) != 0:
            leader.append((grapy.index(i)))
            grapy[grapy.index(i)].append(
                (grapy.index(i), sales[grapy.index(i) - 1]))

    for i in grapy:
        if i:
            i = sorted(i, key=lambda x: x[1])
            team.append(i)

    answer += team[0][0][1]
    minScore = []
    for i in team:
        minScore.append(i[0][1])

    print(minScore)
    print(team)
    print(leader)
    for i in leader[1:]:
        for t in range(len(team)):
            for k in team[t]:
                tempScore = 0
                CommenScore = 0
                if k[0] == i:
                    tempScore += minScore[team.index(team[t])]
    return answer


print(solution(sales, links))