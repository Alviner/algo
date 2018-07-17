# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.value = value
        self.level = 1

    def __iter__(self):
        yield self
        for node in self.left_child:
            yield node
        for node in self.right_child:
            yield node

    def __repr__(self):
        ret = ''
        if self.left_child:
            ret += self.left_child.__repr__()
        ret += f" Node({self.value}) "
        if self.right_child:
            ret += self.right_child.__repr__()
        return ret

    def add(self, other):
        if other < self.value:
            if self.left_child is None:
                self.left_child = TreeNode(other, self)
                self.left_child.reload()
            else:
                self.left_child.add(other)
        else:
            if self.right_child is None:
                self.right_child = TreeNode(other, self)
                self.right_child.reload()
            else:
                self.right_child.add(other)

    def reload(self):
        if self.parent is None:
            self.level = 1
        else:
            self.level = self.parent.level + 1

    def find(self, value):
        if value < self.value:
            if self.left_child is None:
                return self, False, 'left'
            return self.left_child.find(value)
        else:
            if self.value == value:
                return self, True, '-'

            if self.right_child is None:
                return self, False, 'right'
            return self.right_child.find(value)

    def remove(self, value):
        if self.value > value:
            self.left_child = self.left_child.remove(value)
        elif self.value < value:
            self.right_child = self.right_child.remove(value)
        else:
            if self.left_child is None:
                return self.right_child
            elif self.right_child is None:
                return self.left_child

            temp = self.right_child.find_minimum()
            self.value = temp.value
            self.right_child = self.right_child.remove(temp.value)
        return self

    def find_minimum(self):
        if self.left_child is not None:
            return self.left_child.find_minimum()
        else:
            return self

    def find_maximum(self):
        if self.right_child is not None:
            return self.right_child.find_maximum()
        else:
            return self


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        return self.root.__iter__()

    def __repr__(self):
        return self.root.__repr__()

    def add(self, other):
        node, is_exist, pos = self.find(value=other)
        if not is_exist:
            if pos == 'right':
                node.right_child = TreeNode(other, node)
            elif pos == 'left':
                node.left_child = TreeNode(other, node)
            else:
                self.root = TreeNode(other)

    def find(self, value):
        if self.root is not None:
            return self.root.find(value)
        else:
            return None, False, '-'

    def remove(self, value):
        if self.root is not None:
            self.root.remove(value)

    def find_minimum(self):
        if self.root is not None:
            return self.root.find_minimum()

    def find_maximum(self):
        if self.root is not None:
            return self.root.find_maximum()


def test_find():
    tree = BinaryTree()
    tree.add(8)
    tree.add(4)
    tree.add(12)
    tree.add(2)
    tree.add(6)
    tree.add(10)
    tree.add(14)

    node, is_exist, pos = tree.find(8)
    assert node == tree.root and is_exist and pos == '-'

    node, is_exist, pos = tree.find(2)
    assert node == tree.root.left_child.left_child and is_exist and pos == '-'

    node, is_exist, pos = tree.find(3)
    assert node == tree.root.left_child.left_child and not is_exist and pos == 'right'


def test_add():
    tree = BinaryTree()
    tree.add(8)
    tree.add(4)
    tree.add(12)
    tree.add(2)
    tree.add(6)
    tree.add(10)
    tree.add(14)

    assert tree.root.value == 8
    assert tree.root.left_child.value == 4
    assert tree.root.right_child.value == 12
    assert tree.root.left_child.left_child.value == 2
    assert tree.root.left_child.right_child.value == 6


def test_minmax():
    tree = BinaryTree()
    tree.add(8)
    tree.add(4)
    tree.add(12)
    tree.add(2)
    tree.add(6)
    tree.add(10)
    tree.add(14)

    assert tree.find_minimum().value == 2
    assert tree.find_maximum().value == 14
    assert tree.root.right_child.find_minimum().value == 10
    assert tree.root.left_child.find_maximum().value == 6


def test_remove():
    tree = BinaryTree()
    tree.add(8)
    tree.add(4)
    tree.add(12)
    tree.add(2)
    tree.add(6)
    tree.add(10)
    tree.add(14)
    tree.add(1)
    tree.add(3)
    tree.add(5)
    tree.add(7)
    tree.add(9)
    tree.add(11)
    tree.add(13)
    tree.add(15)

    tree.remove(8)
    assert tree.root.value == 9
    tree.remove(12)
    assert tree.root.right_child.value == 13
    tree.remove(1)
    assert tree.root.left_child.left_child.left_child is None


if __name__ == '__main__':
    test_find()
    test_add()
    test_minmax()
    test_remove()
