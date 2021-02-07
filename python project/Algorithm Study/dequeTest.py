from queue import Queue

class Deque(Queue):
    def __init__(self):
        self.items = []
    def enqueue_back(self, item):
        self.items.append(item)

    def dequeue_front(self):
        value = self.items.pop(0)
        if value is not None:
            return value
        else:
            print("Deque is empty.")

    def isEmpty(self):
        return not bool(self.items)

    def enqueue(self, item): 
        self.items.insert(0, item)

    def dequeue(self): 
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Queue is empty.")

    def size(self): 
        return len(self.items)

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("Queue is empty.")

if __name__ == "__main__":
    deque = Deque()
    print("데크가 비었나요? {0}".format(deque.isEmpty()))
    print("데크에 0~9 추가")
    for i in range(10):
        deque.enqueue(i)
    print("데크 크기: {0}".format(deque.size()))
    print("peek: {0}".format(deque.peek()))
    print("dequeue: {0}".format(deque.dequeue()))
    print("peek: {0}".format(deque.peek()))
    print("데크가 비었나요? {0}".format(deque.isEmpty()))
    print()
    print("dequeue: {0}".format(deque.dequeue_front()))
    print("peek: {0}".format(deque.peek()))
    print("enqueue_back(50) 수행")
    deque.enqueue(50)
    print("peek: {0}".format(deque.peek()))
