# -*- coding: utf-8 -*-


class Heap:
    def __init__(self):
        self.values = []

    def _get_left(self, parent):
        return 2 * parent + 1

    def _get_right(self, parent):
        return 2 * parent + 2

    def _get_parent(self, child):
        return int((child - 1) / 2) if (child - 1) / 2 >= 0 else -1

    def _swap(self, index_first, index_second):
        temp = self.values[index_first]
        self.values[index_first] = self.values[index_second]
        self.values[index_second] = temp

    def has_left(self, index):
        return self._get_left(index) < len(self.values)

    def has_right(self, index):
        return self._get_right(index) < len(self.values)

    def has_parent(self, index):
        return self._get_parent(index) >= 0

    def left_child(self, index):
        return self.values[self._get_left(index)]

    def right_child(self, index):
        return self.values[self._get_right(index)]

    def parent(self, index):
        return self.values[self._get_parent(index)]

    def add(self, value):
        self.values.append(value)
        self.heap_up()

    def pop(self):
        if len(self.values) == 0:
            return None
        item = self.values[0]
        self.values[0] = self.values[-1]
        del self.values[-1]
        self.heap_down()
        return item

    def heap_up(self):
        index = len(self.values) - 1
        while self.has_parent(index) and self.parent(index) < self.values[index]:
            self._swap(self._get_parent(index), index)
            index = self._get_parent(index)

    def heap_down(self):
        index = 0
        while self.has_left(index):
            min_child_index = self._get_left(index)
            if self.has_right(index) and self.right_child(index) > self.left_child(index):
                min_child_index = self._get_right(index)

            if self.values[index] > self.values[min_child_index]:
                break
            else:
                self._swap(index, min_child_index)
            index = min_child_index


def test_add():
    heap = Heap()
    heap.add(11)
    heap.add(9)
    heap.add(4)
    heap.add(7)
    heap.add(8)
    heap.add(3)
    heap.add(1)
    heap.add(2)
    heap.add(5)
    heap.add(6)

    test_heap = [
        11,
        9,
        4,
        7,
        8,
        3,
        1,
        2,
        5,
        6
    ]

    for i, i_test in zip(heap.values, test_heap):
        assert i == i_test

    assert heap.left_child(0) == 9
    assert heap.right_child(0) == 4
    assert heap.right_child(heap._get_right(0)) == 1
    assert heap.left_child(heap._get_right(0)) == 3


def test_pop():
    heap = Heap()
    heap.add(11)
    heap.add(9)
    heap.add(4)
    heap.add(7)
    heap.add(8)
    heap.add(3)
    heap.add(1)
    heap.add(2)
    heap.add(5)
    heap.add(6)

    heap_len = len(heap.values)
    heap.pop()

    test_heap = [
        9,
        8,
        4,
        7,
        6,
        3,
        1,
        2,
        5
    ]

    assert len(heap.values) == heap_len - 1

    for i, i_test in zip(heap.values, test_heap):
        assert i == i_test

    assert heap.left_child(0) == 8
    assert heap.right_child(0) == 4
    assert heap.right_child(heap._get_left(0)) == 6
    assert heap.left_child(heap._get_left(0)) == 7


if __name__ == '__main__':
    test_add()
    test_pop()
