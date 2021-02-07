def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]        
        count = 0
        while progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count+=1
            if len(progresses) == 0:
                break
        if count > 0:
            answer.append(count)
    return answer

testProgresses = [93,30,55]
testSpeeds  = [1,30,5]

print(solution(testProgresses,testSpeeds))