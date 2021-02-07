def solution(tickets):
    answer = ["ICN"]
    start = "ICN"

    while len(tickets) != 0:
        sameGroup = []
        rmNum = 0
        #같은 출발지 체크
        for i in range(len(tickets)):
            if tickets[i][0] == start:
                sameGroup.append(i)

        #어딜 먼저갈지 체크
        firstArrive = tickets[sameGroup[0]][1]
        rmNum = sameGroup[0]
        if len(tickets) > 0:
            for i in sameGroup[1:]:
                if tickets[i][1] < firstArrive:
                    firstArrive = tickets[i][1]
                    print(firstArrive)
                    rmNum = i

        #목적지 리스트에 등록
        start = firstArrive
        answer.append(firstArrive)
        tickets.pop(rmNum)
        print(answer)
    return answer

testTickets = 	[["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
print(solution(testTickets))