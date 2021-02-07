def solution(x):
    sum = 0
    for i in range(len(str(x))):
        sum += int(str(x)[i])
    return x % sum == 0 and True

print(solution(11))