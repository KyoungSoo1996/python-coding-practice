# stock : 현재 수량
# dates : 공급 일정
# supplies : 공급 수량
# k : 완료시점


def solution(stock, dates, supplies, k):
    answer = 0
    for day in range(k):
        stock -= 1
        print(str(k - day) + ", " + str(stock))
        if stock >= k - day - 2:
            return answer
        if stock <= 0 and dates[0] - 1 <= day:
            stock = supplies.pop(0)
            dates.pop(0)
            answer += 1
    return answer


testStock = 4
testDates = [4, 10, 15]
testSupplies = [20, 5, 10]
testk = 30

print(solution(testStock, testDates, testSupplies, testk))
