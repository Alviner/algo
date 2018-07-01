# -*- coding: utf-8 -*-

import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, item):
        if 0 > item >= self.count:
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
        if 0 > i >= self.count:
            raise IndexError('Index out of bounds')
        if i == self.count:
            self.append(itm)
            return
        if self.count == self.capacity:
            new_capacity = 2 * self.capacity
        else:
            new_capacity = self.capacity
        new_array = self.make_array(new_capacity)
        for item in range(self.count):
            if item < i:
                new_array[item] = self.array[item]
                continue
            elif item == i:
                new_array[item] = itm
            new_array[item + 1] = self.array[item]
        self.count += 1
        self.array = new_array
        self.capacity = new_capacity

    def delete(self, i):  # O(n)
        if 0 > i >= self.count:
            raise IndexError('Index out of bounds')
        new_array = self.make_array(self.capacity)
        for item in range(self.count - 1):
            if item < i:
                new_array[item] = self.array[item]
            else:
                new_array[item] = self.array[item + 1]
        self.count -= 1
        self.array = new_array
        if self.count <= 2 * self.capacity:
            new_capacity = max(int(2 * self.capacity / 3), 16)
            self.resize(new_capacity)


def test_insert():
    da = DynArray()
    da.insert(0, 1)
    da.insert(0, 2)
    da.insert(1, 4)
    da.insert(2, 6)
    da.insert(2, 8)
    da.insert(1, 0)
    da.insert(2, 3)
    da.insert(4, 5)

    da_test = (2, 0, 3, 4, 5, 8, 6, 1)

    assert len(da_test) == da.count

    for i in range(da.count):
        assert da_test[i] == da[i]


def test_delete():
    da = DynArray()
    da.append(0)
    da.append(1)
    da.append(2)
    da.append(3)
    da.append(4)
    da.append(5)
    da.append(6)
    da.append(7)
    da.append(8)

    da.delete(0)
    da.delete(7)
    da.delete(2)

    da_test = (1, 2, 4, 5, 6, 7)

    assert len(da_test) == da.count

    for i in range(da.count):
        assert da_test[i] == da[i]


if __name__ == '__main__':
    test_insert()
