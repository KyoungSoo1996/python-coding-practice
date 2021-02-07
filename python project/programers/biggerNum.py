# itertools를 사용한 방식 : 시간 초과가 걸린다
# from itertools import permutations


# def solution(numbers):
#     answer = 0
#     numbersToStr = list(map(str, numbers))
#     allCase = list(permutations(numbersToStr, len(numbersToStr)))
#     for i in range(len(allCase)):
#         if answer <= int("".join(allCase[i])):
#             answer = int("".join(allCase[i]))
#     return str(answer)

# def solution(numbers):
#     answer = ''
#     comNumbers = {}
#     for com in range(len(numbers)):
#         temp = numbers[com]
#         while temp / 1000 < 1:
#             temp = temp * 10
#             comNumbers[com] = temp
#     comNumbers = sorted(comNumbers.items(),key=lambda x: x[1]  ,reverse = True)
#     for n in range(len(comNumbers)):
#         answer += str(numbers[comNumbers[n][0]])

#     return answer

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


testNumbers = [6, 10, 2]
print(solution(testNumbers))
