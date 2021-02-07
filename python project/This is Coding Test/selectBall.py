# A, B 두사람이 볼링을 치고 있다.
# 두 사람은 서로 다른 무게를 고르려 한다.
# 공 무게는 번호순으로 부여되며, 같은 무게의 공이 여러 개있지만 서로 다른 공으로 간주
# 볼링공 무게는 1부터 M까지의 자연수 형태
# 서로 다른 무게의 공을 사용할 경우의 수는?

ex1 = [
    [11],
    [7],
    [1,3,2,3,2,2,5,7,3,2,5]
]

ex2 = [
    [8],
    [5],
    [1,5,4,3,2,4,5,2]
]

def SelectBall(N, M, Balls):
    Balls = sorted(Balls)
    print(Balls)
    count = 0
    for i in range(len(Balls)):
        for j in range(i,len(Balls)):
            if Balls[i] != Balls[j]:
                print(i,j)
                count += 1
    return count

def Answer(N,M, Balls):
    array = [0] * 11
    for x in Balls:
        array[x] += 1
    result = 0
    for i in range(1, M[0]+1):
        N[0] -= array[i]
        result += array[i] * N[0]
    return result
    

print(SelectBall(ex1[0],ex1[1],ex1[2]))
print(Answer(ex1[0],ex1[1],ex1[2]))
