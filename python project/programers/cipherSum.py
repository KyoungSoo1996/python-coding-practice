def solution(n):
    sumlist =[]
    for i in range(len(str(n))):
        sumlist.append(int(str(n)[i]))
    return sum(sumlist)

print(solution(123))
