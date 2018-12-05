# -*- coding: utf-8 -*-

import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, item):
        if 0 < item >= self.count:
            raise IndexError('Index out of bounds')
        return self.array[item]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for item in range(self.count):
            new_array[item] = self.array[item]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = item
        self.count += 1

    def insert(self, i, itm):  # O(n)
        if 0 < i > self.count:
            raise IndexError('Index out of bounds')
        if self.count == 0:
            self.append(itm)
            return
        self.append(None)

        for item in reversed(range(self.count)):
            if item > i:
                self.array[item] = self.array[item - 1]
            elif item == i:
                self.array[item] = itm
            else:
                self.array[item] = self.array[item]

    def delete(self, i):  # O(n)
        if 0 > i >= self.count:
            raise IndexError('Index out of bounds')
        for item in range(self.count - 1):
            if item < i:
                continue
            else:
                self.array[item] = self.array[item + 1]
        self.count -= 1
        if self.count <= 2 * self.capacity:
            new_capacity = max(int(2 * self.capacity / 3), 16)
            self.resize(new_capacity)

