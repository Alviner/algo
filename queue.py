# -*- coding: utf-8 -*-

from stack import Stack


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):  # O(n)
        self.items.insert(0, item)

    def dequeue(self):  # O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)

    def rotate(self, N):
        for i in range(N):
            self.enqueue(self.dequeue())


class StackQueue:
    def __init__(self):
        self.right = Stack()
        self.left = Stack()

    def enqueue(self, item):
        self.right.push(item)

    def dequeue(self):
        if self.left.size() == 0:
            while self.right.size() > 0:
                self.left.push(self.right.pop())
        return self.left.pop()

    def rotate(self, N):
        for i in range(N):
            self.enqueue(self.dequeue())

    def size(self):
        return self.right.size() + self.left.size()


def test_rotate():
    qu = Queue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)

    qu_stack = StackQueue()
    qu_stack.enqueue(1)
    qu_stack.enqueue(2)
    qu_stack.enqueue(3)
    qu_stack.enqueue(4)

    qu.rotate(22)
    qu_stack.rotate(22)

    qu_test = Queue()
    qu_test.enqueue(3)
    qu_test.enqueue(4)
    qu_test.enqueue(1)
    qu_test.enqueue(2)

    assert qu.size() == qu_test.size() == qu_stack.size()

    while qu.size() > 0:
        assert qu.dequeue() == qu_test.dequeue() == qu_stack.dequeue()


if __name__ == '__main__':
    test_rotate()
