# 두 개의 배열 A와 B가 있다.
# A와 B의 원소를 하나씩 골라 두 원소를 바꾼다.
# 이때 A의 모든 원소의 합이 최대가 되게 만들어라.

# 첫 번째 줄에 N, K가 공백으로 구분되어 입력된다.
# 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
# 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하라.

#N : 갯수, K : 횟수
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(K):
    swapA = min(a)
    swapB = max(b)
    a[a.index(swapA)], b[b.index(swapB)] = swapB, swapA
print(sum(a))