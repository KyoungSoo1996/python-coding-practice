def solution(n):
    fibo = [0,1]
    for i in range(1,n+1):
        fibo.append(fibo[i-1] + fibo[i])
    return fibo[-1] % 1234567

testN = 3

print(solution(testN))