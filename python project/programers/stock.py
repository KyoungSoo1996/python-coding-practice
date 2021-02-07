from collections import deque

def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        for n in range(i, len(prices)):
            if prices[n] >= prices[i]:
                count += 1
            else:
                count += 1
                break
        answer.append(count-1)
    return answer

def stack_solution(price):
    answer =[]
    prices = deque(price)
    while prices:
        c = prices.popleft()
        count = 0
        for i in prices:
            if c > i :
                count += 1
                break
            count += 1
        answer.append(count)
    return answer


testPrices = [5, 4, 3, 5, 6, 5]
print(solution(testPrices))
print(stack_solution(testPrices))