import collections

#remove를 사용하면 효율성이 떨어진다. 그럼 어떻게?
# def solution(participant, completion):
#     for i in range(len(completion)):
#             participant.remove(completion[i])
#     return ' '.join(participant)

#해쉬를 사용해보자


def solution(participant, completion):
    answer = ''
    dictionary = {}
    for i in participant:
        if i in dictionary:
            dictionary[i] = dictionary[i]+1
        else:
            dictionary[i] = 1

    for i in completion:
        if i in dictionary:
            dictionary[i] = dictionary[i] - 1

    for name, count in dictionary.items():
        if count == 1:
            answer += name + " "
    return answer


def best_solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())

testParticipant = ['leo', 'kiki', 'eden']
testCompletion = ['eden']

print(solution(testParticipant, testCompletion))
print(best_solution(testParticipant,  testCompletion))
