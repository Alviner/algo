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
        return self.items.__len__()

    def __len__(self):
        return self.items.__len__()

    def rotate(self, N):
        for i in range(N):
            self.enqueue(self.dequeue())


class StackQueue:
    def __init__(self):
        self.right = Stack()
        self.left = Stack()

    def enqueue(self, item):  # O(n)
        self.right.push(item)

    def dequeue(self):  # O(n)
        if self.left.size() == 0:
            while self.right.size() > 0:
                self.left.push(self.right.pop())
        return self.left.pop()

    def rotate(self, N):
        for i in range(N):
            self.enqueue(self.dequeue())

    def size(self):
        return self.right.size() + self.left.size()

