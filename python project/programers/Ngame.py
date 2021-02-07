def solution(n, t, m, p):
    answer = ''
    text = ''
    count = 0
    while len(text) < t * m:
        temp = convert(count, n)
        text += temp
        if len(answer) < t:
            count += 1
    for i in range(len(text)) :
        if i%m == p-1:
            answer += text[i]
            if len(answer) == t:
                return answer

#진법 변환해주는 함수
def convert(number, N):
    #16 진수 이므로 15개만
    num = '0123456789ABCDEF'
    va, lo = divmod(number, N)
    if va == 0:
        return num[lo]
    else:
        return convert(va, N) + num[lo]

testN = 2
testT = 4
testM = 2
testP = 1
print(solution(testN,testT,testM,testP))