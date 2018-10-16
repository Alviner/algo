# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.value = value
        self.level = 1

    def __repr__(self):
        return f'Node({self.value})'


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self, node=None):
        if node is None:
            node = self.root
        yield node
        if node.left_child:
            for item in self.__iter__(node.left_child):
                yield item
        if node.right_child:
            for item in self.__iter__(node.right_child):
                yield item

    def __repr__(self, node=None):
        if node is None:
            node = self.root
        ret = ''
        if node.left_child:
            ret += self.__repr__(node.left_child)
        ret += node.__repr__()
        if node.right_child:
            ret += self.__repr__(node.right_child)
        return ret

    def reload(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.parent is None:
            node.level = 1
        else:
            node.level = node.parent.level + 1
        if node.left_child is not None:
            self.reload(node.left_child)
        if node.right_child is not None:
            self.reload(node.right_child)

    def add(self, other, node=None):
        if node is not None:
            is_exist, pos = False, 'right' if node.right_child is None else 'left'
        else:
            node, is_exist, pos = self.find(value=other)
        if not is_exist:
            if pos == 'right':
                node.right_child = TreeNode(other, node)
                self.reload(node.right_child)
                return node.right_child
            elif pos == 'left':
                node.left_child = TreeNode(other, node)
                self.reload(node.left_child)
                return node.left_child
            else:
                self.root = TreeNode(other)
                return self.root

    def find(self, value, node=None):
        if node is None:
            node = self.root
        if node is None:
            return node, False, '-'
        if value < node.value:
            if node.left_child is None:
                return node, False, 'left'
            return self.find(value, node.left_child)
        else:
            if node.value == value:
                return node, True, '-'

            if node.right_child is None:
                return node, False, 'right'
            return self.find(value, node.right_child)

    def remove(self, value, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node.value > value:
            successor = self.remove(value, node.left_child)
            if successor is not None:
                successor.parent = node
            node.left_child = successor
        elif node.value < value:
            successor = self.remove(value, node.right_child)
            if successor is not None:
                successor.parent = node
            node.right_child = successor
        else:
            if node.left_child is None:
                return node.right_child
            elif node.right_child is None:
                return node.left_child

            temp = self.find_minimum(node.right_child)
            node.value = temp.value
            successor = self.remove(temp.value, node.right_child)
            successor.parent = node
            node.right_child = successor
        return node

    def find_minimum(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return node
        if node.left_child is not None:
            return self.find_minimum(node.left_child)
        else:
            return node

    def find_maximum(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return node
        if node.right_child is not None:
            return self.find_maximum(node.right_child)
        else:
            return node


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
    assert tree.find_minimum(tree.root.right_child).value == 10
    assert tree.find_maximum(tree.root.left_child).value == 6


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
    assert tree.root.left_child.parent is tree.root
    assert tree.root.right_child.parent is tree.root


if __name__ == '__main__':
    test_find()
    test_add()
    test_minmax()
    test_remove()
