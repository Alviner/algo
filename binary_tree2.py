# -*- coding: utf-8 -*-


class BinaryTree:
    def __init__(self):
        self.values = []

    def add(self, value):
        node = self.find(value)
        if node is None:
            self.values.append(value)
            node = 0
        if node < 0:
            self.values[-node] = value
        self.values.insert(2 * (-node) + 1, None)
        self.values.insert(2 * (-node) + 2, None)

    def find(self, value):
        pos = 0
        if len(self.values) == 0:
            return None
        while pos < len(self.values):
            if self.values[pos] is None:
                pass
            elif value < self.values[pos]:
                left_child = 2 * pos + 1
                if self.values[left_child] is None:
                    return - left_child
                pos = left_child
            else:
                if self.values[pos] == value:
                    return pos
                right_child = 2 * pos + 2
                if self.values[right_child] is None:
                    return - right_child
                pos = right_child


def test_add():
    tree = BinaryTree()
    tree.add(50)
    tree.add(75)
    tree.add(25)
    tree.add(37)
    tree.add(62)
    tree.add(84)
    tree.add(31)
    tree.add(43)
    tree.add(55)
    tree.add(92)

    test_tree = [
        50,
        25,
        75,
        None,
        37,
        62,
        84,
        None,
        None,
        31,
        43,
        55,
        None,
        None,
        92
    ]

    for test, val in zip(test_tree, tree.values[:len(test_tree)]):
        assert test == val

    assert tree.find(22) == -3
    assert tree.find(63) == -12
    assert tree.find(83) == -13
    assert tree.find(92) == 14


if __name__ == '__main__':
    test_add()


