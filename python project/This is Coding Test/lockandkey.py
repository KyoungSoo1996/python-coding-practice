key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key, lock):
    # print(lock)
    if len(lock) - len(key) == 0:
        for i in range(0, 4):
            key = SpinList(key)
            if SumList(key, lock,0,0):
                return True    
    else:
        for x in range(0, (len(lock) - len(key)+1)):
            for y in range(0, (len(lock) - len(key)+1)):
                for i in range(0, 4):
                    key = SpinList(key)
                    if SumList(key, lock,x,y):
                        return True
    return False


def SpinList(key):
    resultList = []
    for i in range(len(key)-1,-1,-1):
        temp = []
        for j in range(len(key)):
            temp.append(key[j][i])
        resultList.append(temp)
    return resultList


def SumList(key, lock, x, y):
    sumList = lock

    for i in range(0, len(key)):
        for j in range(0, len(key)):
            sumList[i+x][j+y] = key[i][j] + lock[i+x][j+y]
    for i in range(len(sumList)):
        for j in range(len(sumList[0])):
            print(sumList)
            if sumList[i][j] == 0 or 2:
                return False
        return True

    if sum(lock):
        return True
    else:
        return False

print(solution(key,lock))