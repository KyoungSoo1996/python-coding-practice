# N = 4이고 각 위치가 1,5,7,9일때
# 안테나를 5에 설치할 때, 거리의 총합이 4+9+2+4 = 10으로 최소이다.

house = [5,1,7,9]

def Antenna(house):
    answer = []
    for i in house:
        temp = 0
        for j in house[0:i] + house[i+1:]:
            if i > j:
                temp += (i - j)
            else:
                temp += (j - i)
                
        answer.append(temp)
    return house[answer.index(min(answer))]
    
print(Antenna(house))
