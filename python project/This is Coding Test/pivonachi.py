#피보나치 수열 구현하기
import time
def pivonachi(n):
    if n == 1 or n ==2:
        return 1
    return pivonachi(n - 1) + pivonachi(n -2)
end_time = time.time()

# print(pivonachi(30))

# 위와 같이 피보나치 수열을 구현했을 때, 시간 복잡도는 기하급수적으로 증가한다.
# 그 이유는 중복되는 계산이 많아서이고, 이를 방지하기 위해서 다이나믹 프로그래밍을 사용한다.
# 다이나믹 프로그래밍을 사용하기 위해서는 2개의 규칙이 있어야한다.

# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# 피보나치 수열은 이 조건에 부합하고, 메모이제이션 기법으로 해결할 수 있다.
# 이는 한 번 구한 결과를 메모리에 저장해두고 같은 식이면 다시 호출하는 방식이다.

d = [0] * 101
def fibonachi(x):
    d[1] = 1
    d[2] = 1
    d[x] = d[x-1] + d[x-2]
    return fibonachi(d[x])

print(fibonachi(100))