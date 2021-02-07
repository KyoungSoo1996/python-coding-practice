#공통된 인자중 최대로 높일 수 있는 값에다가 나눈 값들을 곱했다.
#테스트 2개는 통과했지만 다음에서 막힌다.

# def solution(arr):
#     pro = 1
#     divList = []
#     num = 1
#     for i in range(2,min(arr)+1):
#         for j in arr:
#             if j%i == 0:
#                 divList.append(j/i)
#                 if len(divList) == len(arr):
#                     num = i
#             else:
#                 del divList[:]    
#     if len(divList) == len(arr):
#         for p in divList:
#             pro *= p
#     elif len(divList) == 0:
#         for p in arr:
#             pro *= p
#     return int(pro * num)

# 2개씩 최소공배수를 구한 다음에 연쇄적으로 구한다
def leastCommon(arr):
    a, b = max(arr[0],arr[1]), min(arr[0],arr[1])
    while b > 0:
        a, b = b, a%b
    return a

def solution(arr):
    while len(arr) != 1:
        temp = []
        i = arr.pop()
        j = arr.pop()
        temp.append(i)
        temp.append(j)
        k = leastCommon(temp)
        arr.insert(0,int(i*j/k))
    return (arr[0])

from fractions import gcd

def best_solition(arr):
    answer = arr[0]
    for n in arr:
        answer = n * answer/ gcd(n, answer)
    return answer


testArr = [1,2,3]
testArr2 = [6,3]
print(solution(testArr))
print(best_solition(testArr))