#fibo
# def solution(n):
#     fibo = [0, 1]
#     for i in range(2,n + 1):
#         fibo.append(fibo[i-2]+fibo[i-1])
#     return fibo[n]%1234567

#tiling
def solution(n):
    fibo = [0, 1]
    n = n+1
    for i in range(2,n + 1):
        fibo.append((fibo[i-2]+fibo[i-1]) % 1000000007)
    return fibo[n]

tsetN = 4
print(solution(tsetN))