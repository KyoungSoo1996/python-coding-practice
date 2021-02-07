class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value): #데이터 삽입
        self.items.append(value)
    
    def pop(self): #데이터 반환 및 제거
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack is empty.")

    def size(self): #스택 크기 조회
        return len(self.items)

    def peek(self): #스택 끝 항목 조회
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty")

    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        stack.push(i)
    print("스택 크기 : {0}".format(stack.size()))
    print("peek: {0}".format(stack.peek()))
    print("pop: {0}".format(stack.pop()))
    print("peek: {0}".format(stack.peek()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack)

    