def solution(n):
    answer = ''
    stack = []
    while 1:
        if n >= 3:
            if n%3 != 0:
                stack.append(n % 3)
                n = n//3
            else :
                stack.append(4)
                n = n//3 -1
        else : 
            stack.append(n)
            break
    for i in range(len(stack)):
        answer += str(stack.pop())
    return answer.lstrip('0')


def best_solution(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n %3] + answer
        n//= 3
    return answer

testN = 3
print(solution(testN))
print(best_solution(testN))