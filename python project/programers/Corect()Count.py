def solution(n):
    answer = 0
    #Catalan
    return factorial(2*n)//(factorial(n) * factorial(n+1))

#factorial function
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact
    
testN = 3
print(solution(testN))