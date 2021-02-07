def grouping(str):
    temp = []
    for i in range(1, len(str)):
        tempstr = str[i - 1] + str[i]
        if tempstr.isalpha():
            temp.append(tempstr.upper())
    return temp


def solution(str1, str2):
    gstr1 = grouping(str1)
    gstr2 = grouping(str2)
    num = len(gstr2)
    t = gstr1 + gstr2  # 전체의 합집합
    for i in gstr1:
        if i in gstr2:
            gstr2.remove(i)
    if len(t) - (num - len(gstr2)) == 0:
        return 65536
    if num - len(gstr2) == 0:
        return 0

    return int((num - len(gstr2)) / (len(t) - (num - len(gstr2))) * 65536)


testStr1 = "E=M*C^2"
testStr2 = "e=m*c^2"
print(solution(testStr1, testStr2))

