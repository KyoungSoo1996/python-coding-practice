def solution(priorities, location):
    finList = []
    pointList = [0]
    pointList += set(priorities)
    pointList = sorted(pointList, reverse= True)
    while len(pointList) != 0:
        if pointList[0] == 0:
            break
        for i in range(len(priorities)):
            if pointList[0] == priorities[i]:
                priorities[i] = 0
                finList.append(i)
            if pointList[0] not in priorities:
                pointList.pop(0)
            if  sum(priorities) == 0:
                break
    return finList.index(location) + 1


testPriorities = [2,1,3,2]
testLocation = 2

print(solution(testPriorities, testLocation))
