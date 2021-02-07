# 알파벳 대문자와 숫자(0~9)가 주어질 경우, 대문자로 정렬한 후 모든 숫자를 더한 값을 앞에 두시오.

text = 'K1KA5CB7'
text2 = 'AJKDLSI412K4JSJ9D'
isnum = ['1','2','3','4','5','6','7','8','9','0']
def ReSort(text):
    countNum = 0
    sumNum = 0
    for i in text:
        if i in isnum:
            countNum += 1
            sumNum += int(i)
            
    result = sorted(text)[countNum:]
    return ''.join(result) + str(sumNum)

print(ReSort(text2))