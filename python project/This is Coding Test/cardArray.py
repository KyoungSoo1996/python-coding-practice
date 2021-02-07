# 첫째 줄에 N이 주어집니다.(1 <= N <= 100,000) 이어서 N개의 줄에 걸쳐 숫자 카드 묶음의 크기가 주어진다.

cards = [10,20,40,50]

def CardArray(cards):
    cards = sorted(cards)
    result = cards[0] + cards[1]
    for i in cards[2:]:
        result += result + i
    return result
print(CardArray(cards))
    
    
import heapq

def Answer(cards):
    heap = []
    for i in cards:
        heapq.heappush(heap, i)
    
    result = 0

    while len(heap) != 1:
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        sum_value = one + two
        result += sum_value
        heapq.heappush(heap,sum_value)
    return result

print(Answer(cards))