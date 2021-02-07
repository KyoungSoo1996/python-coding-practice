def solution(n, lost, reserve):
    lostCloth =[]
    reserveCloth = []
    finalCloth = []
    #리스트 초기화
    for i in range(0,n):
        finalCloth.append(0)
        lostCloth.append(1)
        reserveCloth.append(0)

    #체육복 잃어버렸다 거수(전체 리스트로 활용)
    for i in lost:
        lostCloth[i-1] = 0
   
    #여분 가져왔다 거수
    for i in reserve:
        reserveCloth[i-1] = 1

    #잃어버렸지만 자신이 여분 체육복이 있다 거수
    for i in range(0,n):
        if lostCloth[i] == 0:
            if reserveCloth[i] == 1:
                reserveCloth[i] = 0
                lostCloth[i] = 1

    #앞사람에게 빌려줄 여분이 있다 거수
    for i in range(1,n):
        if lostCloth[i-1] == 0:
            if reserveCloth[i] == 1:
                reserveCloth[i] = 0
                lostCloth[i-1] = 1

    #뒷사람에게 빌려줄 여분이 있다 거수
    for i in range(0,n-1):
        if lostCloth[i+1] == 0:
            if reserveCloth[i] == 1:
                reserveCloth[i] = 0
                lostCloth[i+1] = 1

    return sum(lostCloth)

def best_solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [i for i in lost if i not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
testn = 3
testLost = [2,3]
testReserve = [1]

print(solution(testn, testLost, testReserve))
print(best_solution(testn, testLost, testReserve))
