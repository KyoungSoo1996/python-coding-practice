from collections import deque

queue = deque()
queue.append(5)
print(queue)
queue.append(3)
print(queue)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
queue.append(1)
print(queue)
queue.append(4)
print(queue)
queue.popleft()
print(queue)

queue.reverse()
print(queue)