from collections import deque

def solution(operations):
    queue = deque()
    answer = []
    for operation in operations:
        if operation.split()[0] == 'I':
            queue.append(operation.split()[1])
        elif operation.split()[0] == 'D':
            if operation.split()[1] == 1:
        
    return answer