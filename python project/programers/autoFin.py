def check(words, word):
    return str(words).count(word)


def solution(words):
    answer = 0
    for word in range(len(words)):
        for i in range(len(words[word])):
            if check(words, words[word][:i]) == 1:
                break
            else:
                answer += 1

    return answer


testWord = ["abc", "def", "ghi", "jklm"]

print(solution(testWord))
