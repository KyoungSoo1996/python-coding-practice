# 정렬을 해서 가장 큰 것과 가장 작은 것을 태워 보낸다.
def solution(people, limit):
    people.sort()
    boatCnt = 0
    inboat = 0
    peopleCnt = len(people) - 1
    while inboat <= peopleCnt:
        boatCnt += 1
        if people[peopleCnt] + people[inboat] <= limit:
            inboat += 1
        peopleCnt -= 1

    return boatCnt


testPeople = [70, 80, 50, 50]
tsetLimit = 100
print(solution(testPeople, tsetLimit))
