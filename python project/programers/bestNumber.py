def solution(n: int) -> int:
    numbers = []
    for num in range(0, 10):
        if (n // 10**(9-num)) > 0:
            numbers.append(n//10**(9-num))
            n -= n//10**(9-num) * 10**(9-num)
    return sorted(numbers, reverse= True)


print(solution(23123123))
