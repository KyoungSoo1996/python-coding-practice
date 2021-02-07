def solution(n):
    temp = bin(n)
    brk = temp.count("1")
    k = 0
    while brk != k:
        n += 1
        k = bin(n).count("1")
    return n


print(solution(78))
