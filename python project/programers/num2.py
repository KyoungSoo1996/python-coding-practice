# orders 배열의 크기는 2이상 20이하이다.
# orders 배열의 각 원소는 크기가 2이상 10이하이다.
# 각 문자열은 알파벳 대문자로만 이루어져있다.
# 각 문자열에는 같은 알파벳이 중복해서 들어있지 않다.

# courese 배열의 크기는 1이상 10이하이다.
# 자연수가 오름차순으로 정렬되어있다.
# 배열에 담아 사전 순으로 오름차순 정렬해서 return 하라

# 단 코스요리 멘뉴는 최소 2가지 이상의 단품 메뉴로 구성한다.
# 최소 2명 이상의  손님에게서 주문된 구성요리만 코스요리 후보에 들어간다.

import itertools
from collections import Counter
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 4]


def solution(orders, course):
    for i in range(len(orders)):
        orders[i] = sorted(orders[i])
    answer = []
    ordersUnion = [] * len(orders)
    for i in course:
        for j in orders:
            ordersUnion += list(map(''.join, itertools.combinations(j, i)))
        temp = Counter(ordersUnion).most_common()
        for num in temp:
            if num[1] >= temp[0][1] and temp[0][1] >= 2:
                answer.append(num[0])
        ordersUnion.clear()

    return sorted(answer)


print(solution(orders, course))