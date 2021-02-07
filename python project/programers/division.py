def solution(arr, divisor):
    answer = []
    for num in arr:
        if(num % divisor == 0):
            answer.append(num)
    if(len(answer) == 0):
        answer.append(-1)

    return sorted(answer)


def best_solution(arr, divisor): return sorted(
    [n for n in arr if n % divisor == 0]) or [-1]


testArr = [2, 36, 1, 3]
testdivisor = 2

print(solution(testArr, testdivisor))
print(best_solution(testArr,testdivisor))