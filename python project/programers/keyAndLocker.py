def solution(key, lock):
    # print(lock)
    if SumList(key, lock):
        return True
    else:
        #90도 회전
        for i in range(0, 4):
            if SumList(SpinList(key), lock):
                return True
        return False


def SpinList(list1):
    resultList = []
    for i in range(0, 3):
        temp = []
        for j in range(0, 3):
            temp.append(list1[2 - j][i])
        resultList.append(temp)
    return resultList


def SumList(list1, list2):
    sumList = []
    temp = []
    for i in range(0, 3):
        temp.clear()
        for j in range(0, 3):
            temp.append(list1[i][j] or list2[i][j])
        sumList.append(temp)
    if sumList == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]:
        return True
    else:
        return False


print(solution(key, lock))
