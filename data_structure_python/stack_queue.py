
class Stack():
    # 지원하는 연산 : push, pop, top, empty
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self._is_empty():
            print("stack is empty!")
            return None
        else:
            return self.stack.pop()

    def top(self):
        if self._is_empty():
            print("stack is empty!")
            return None
        else:
            return self.stack[-1]

    def _is_empty(self):
        return False if self.stack else True


class Queue():
    # 지원하는 연산 : enqueue, dequeue, peek, empty
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self._is_empty():
            print("queue is empty!")
            return None
        else:
            return self.queue.pop(0) # 0 인덱스 pop

    def peek(self):
        if self._is_empty():
            print("queue is empty!")
            return None
        else:
            return self.queue[0]

    def _is_empty(self):
        return False if self.queue else True


# TODO : Singly linked list 로 구현해보기?