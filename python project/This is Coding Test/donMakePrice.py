# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하시오.
# ex) N = 5이고 각 동전이 3,2,1,1,9원짜리 동전일 경우
#     만들 수 없는 양의 정수 금액 중 최솟값은 8원이다.

#start time : 2:08

money = [3,2,1,1,9]
# def DMakePrice(moneys):
#     money = sorted(moneys)
#     for i in range(1, sum(money)):
#         sumMoney = 0
#         for k in money:
#             sumMoney += k
#             if i == sumMoney:
#                 continue
#         return i

# print(DMakePrice(money))

def DMakePrice(moneys):
    moneys = sorted(moneys)
    target = 1
    for x in moneys:
        if target < x:
            break
        target += x
    return target
print(DMakePrice(money))

# 정렬을 이용한 그리디 알고리즘으로 해결할 수 있는 문제이다.
# 일단 동전에 대한 정보가 주어지면, 화폐 단위를 기준으로 오른차순 정렬한다.
# 1부터 현재 가지고 있는 동전으로 만들 수 있는 금액을 업데이트 해주면된다.
# target은 모든 숫자를 만들 수 있는 경우의 수이다.

def DMake(moneys):
    moneys = sorted(moneys)
    target = 1
    for i in moneys:
        if target < i:
            break
        else:
            target += i
    return target

print(DMake(money))

