def solution(heights):
    answer = []
    temp = []
    for i in range(len(heights)):
        for n in range(0,i):
            if heights[i] < heights[n]:
                temp.append(n)
        if len(temp) == 0:
            answer.append(0)
        else :
            answer.append(max(temp)+1)
            temp = []
    return answer

testHeights = [3,9,9,3,5,7,2]
print(solution(testHeights))