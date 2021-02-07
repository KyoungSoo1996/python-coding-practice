1. 재귀함수를 사용한 피보나치
-> 구현하기 쉬움, 계산량이 많아 수가 커지면 효율 떨어집니다.

def Fibonacci(num):
    if num == 0:
        return 0
    elif num in (1, 2):
        return 1
    return Fibonacci(num - 1) + Fibonacci(num - 2)


2. 다이나믹 프로그래밍을 이용한 피보나치
-> 구현하기 어려움, 한번 계산한 연산은 생략할 수 있음 효율이 좋아집니다.


def DynamicFibonacci(num):
    global array
    if num == 0:
        return 0
    elif num in (1, 2):
        return 1
    else:
        array = [0] * (num + 1)
        array[1] = 1
        array[2] = 1
        for i in range(3, num + 1):
            array[i] = array[i - 1] + array[i - 2]
        return array[num]


print(DynamicFibonacci(6))