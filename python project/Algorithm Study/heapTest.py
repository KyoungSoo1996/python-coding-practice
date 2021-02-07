import heapq
# listTest = [4, 6, 8, 1]
# heapq.heapify(listTest)
# print(listTest)

h = []
heapq.heappush(h, (1, 'food'))
heapq.heappush(h, (2, 'work'))
heapq.heappush(h, (3, 'sport'))
heapq.heappush(h, (4, 'awake'))
print(h)