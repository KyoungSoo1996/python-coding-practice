import time

#큰 수의 법칙은 일반적으로 통게 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다.
#동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
#단, 배열의 특정한 인덱스 (번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

#입력 조건
#첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <=10,000), K(1 <= K 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다. 

#N : 배열, M : 숫자가 더해지는 횟수, K : 반복할 수 있는 수

def Function(N, M, K):
    start_time = time.time()
    result = 0
    sortedList = sorted(N, reverse=True)
    if sortedList[0] == sortedList[1]:
        result = sortedList[0] * M
    else:
        for i in range(0, M):
            if i%(K+1) == 0:
                result += sortedList[1]
            else:
                result += sortedList[0]
    end_time = time.time()
    print(end_time - start_time)
    return result

print(Function([2,4,5,4,6], 8, 3))

#Firest Answer
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# start_time = time.time()
# data.sort()
# first = data[n - 1]
# second = data[n - 2]

# result = 0
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
# end_time = time.time()
# print(end_time - start_time)
# print(result)

#Second Answer
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
first_time = time.time()
data = sorted(data)
first = data[n - 1]
second = data[n- 2]
num = m//(k+1)
end_time = time.time()
print(end_time - first_time)
print(num)
print(first *(m-num) + second * num)
