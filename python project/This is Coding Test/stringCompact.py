# 압축할 문자열 s가 매개변수로 주어질 때, 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하시오.


def solution(s):
    CompactStr = []
    count = []
    rm = 0
    for i in range(1,len(s)//2+1):
        for j in range(0, len(s)):
            if len(s[j*i:(j+1)*i]) == i:
                CompactStr.append(s[j*i:(j+1)*i])
        rm = len(s) - i * len(CompactStr)
        temp = 0
        tempList = []
        sub = 0
        print(CompactStr)
        for k in range(len(CompactStr)):
            if k == len(CompactStr) - 1:
                tempList.append(temp)
                temp = 0                
                sub += 1
                break
            if CompactStr[k] == CompactStr[k+1]:
                # 압축된 경우
                temp += 1                
            else:
                print(k == len(CompactStr) -1)
                tempList.append(temp)
                temp = 0                
                sub += 1
        count.append(len(s) - (sum(tempList) * len(CompactStr[0]) + rm) + sum(tempList))
        CompactStr.clear()
    return count
            
print(solution('xababcdcdababcdcd'))