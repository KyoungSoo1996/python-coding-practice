def solution(n, words):
    answer = []
    readWords = []
    userNum = 0
    readWords.append(words[0])
    for i in range(1, len(words)):
        turn = i//n + 1
        userNum = i % n
        if readWords[-1][-1] != words[i][0] or readWords.count(words[i]) >= 1:
            answer.append(userNum+1)
            answer.append(turn)
            break
        else:
            readWords.append(words[i])
    if len(answer) == 0:
        answer = [0, 0]

    return answer

testN = 3
testWords = ['tank', 'kick', 'know', 'wheel',
             'land', 'dream', 'mother', 'robot', 'tank']
testN2 = 2
testWords2 = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(testN2, testWords2))
