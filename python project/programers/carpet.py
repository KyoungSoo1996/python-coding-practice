
def solution(brown, red):
    answer = []
    #두변의 합
    RowPlusCol = (brown - 4)//2
    a = 1
    b = -RowPlusCol
    c = red
    #근의 공식
    value = int((b*b -4*a*c)**0.5)
    answer.append(int((-b + value)/(2*a))+2)
    answer.append(int((-b-value)/(2*a))+2)
    return answer
testBrown = 24
testRed = 24
print(solution(testBrown, testRed))
