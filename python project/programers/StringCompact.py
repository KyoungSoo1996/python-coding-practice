#문제 잘못 풀었음 ㅠㅠ
# def solution(s):
#     answer = 0
#     compactSize = len(s)//2
#     tempWord = {}

#     for i in range(1, compactSize):
#         for n in range(len(s)//i):
#             if s[n*i:(n+1)*i] not in tempWord:
#                 tempWord[s[n*i:(n+1)*i]] = 0
#             else:
#                 tempWord[s[n*i:(n+1)*i]] += 1

#         print(tempWord)

#         tempWord = {}
#     return answer


def solution(s):
    stringLenCount = []
    compactSize = len(s)//2 + 1
    if(len(s) == 1):
        return 1
    for i in range(1, compactSize):
        stack = ['']
        count = [0] * int(len(s)//i)
        for n in range(len(s)//i):
            if s[n*i:(n+1)*i] == stack[-1]:
                count[n] = 1
            else:
                stack.append(s[n*i:(n+1)*i])
        if i * int(len(s)//i) < len(s):
            stack.append(s[i * int(len(s)//i):])
        stack.pop(0)

        for i in range(len(count)):
            if count[i] >= 1 and i+1 < len(count):
                if count[i+1] == 1:
                    count[i+1] += count[i]
                    count[i] = 0
        data = 0
        for i in count:
            if i == 1:
                data +=1
            elif i > 1:
                data += len(str(count[i] + 1))
        stringLenCount.append(len(''.join(stack))+ data)
    return min(stringLenCount)


def best_solution(s):
    def compress(length):
        n = 0
        before, count = s[:length], 1
        for i in range(length, len(s), length):
            word = s[i:i+length]
            if word == before:
                count += 1
            else:
                if count > 1:
                    n += len(str(count))
                n += length
                before, count = word, 1
        if count > 1:
            n += len(str(count))
        n += len(before)
        return n

    anser = len(s)
    for length in range(1, anser+2//2):
        anser = min(anser, compress(length))
    return anser

testS = 'aabbaccc'
print(best_solution(testS))
print(solution(testS))
