# -*- coding: utf-8 -*-


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



