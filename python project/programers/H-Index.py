def solution(citations):
    sw = True
    h = 0
    while sw:
        tempHCount = 0
        for i in citations:
            if h <= i:
                tempHCount +=1
        if tempHCount >= h:
            h +=1
        else :
            sw = False
            return h-1



testCitations = [3, 0, 6, 1, 5]
print(solution(testCitations))
