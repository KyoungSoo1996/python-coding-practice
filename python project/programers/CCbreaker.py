def solution(s):
    temp = []
    for i in s:
        if len(temp) == 0:
            temp.append(i)
        else:
            if temp[-1] == i:
                temp.pop(-1)
            else:
                temp.append(i)
    if len(temp) == 0:
        return 1
    else:
        return 0


testS = "abdabb"
print(solution(testS))
