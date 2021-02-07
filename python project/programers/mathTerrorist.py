#수포자 1 : 1,2,3,4,5,1,2,3,4,5...
#수포자 2 : 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5
#수포자 3 : 3,3,1,1,2,2,4,4,5,5


def solution(answers: list):
    answer = []
    count = 0
    answerOK = [0, 0, 0]
    firstTerrorist = [1, 2, 3, 4, 5]
    secondTerrorist = [2, 1, 2, 3, 2, 4, 2, 5]
    thridTerrorist = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for num in range(len(answers)):
        if answers[num] == firstTerrorist[num % 5]:
            answerOK[0] += 1
        if answers[num] == secondTerrorist[num % 8]:
            answerOK[1] += 1
        if answers[num] == thridTerrorist[num % 10]:
            answerOK[2] += 1
    maxTerroristScore = max(answerOK)
    for i in answerOK:
        count += 1
        if i == maxTerroristScore:
            answer.append(count)
    return answer


def best_solution(answer):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answer):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


new = [1, 2, 3, 4, 5, 2, 5, 2, 2, 1, 4, 2, 5, 2, 3, 1, 3, 4]

print(solution(new))
print(best_solution(new))