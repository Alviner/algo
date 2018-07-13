# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, value, parent):
        self.parent = parent
        self.child = []
        self.value = value
        self.level = 1

    def __iter__(self):
        yield self
        for item in self.child:
            for node in item:
                yield node

    def __repr__(self):
        ret = "\t" * (self.level - 1) + repr(self.value) + "\n"
        for item in self.child:
            ret += item.__repr__()
        return ret

    def add(self, new_node):
        self.child.append(new_node)

    def reload(self):
        if self.parent is None:
            self.level = 1
        else:
            self.level = self.parent.level + 1


class SimpleTree:
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return self.root.__iter__()

    def __repr__(self):
        return self.root.__repr__()

    def add(self, node, child_node):
        child_node.parent = node
        if node is not None:
            node.add(child_node)
            self.reload(node)
        else:
            self.root = child_node

    def reload(self, node=None):
        if node is None:
            for item in self:
                item.reload()
        else:
            for item in node:
                item.reload()

    def remove(self, node):
        if node.parent is not None:
            node.parent.child.remove(node)
        else:
            self.root = None

    def find(self, value):
        res = []
        for item in self:
            if item.value == value:
                res.append(item)
        return res

    def move(self, node, node_move):
        self.remove(node_move)
        self.add(node, node_move)

    def count(self):
        nodes = 0
        leafs = 0
        for item in self:
            nodes += 1
            if len(item.child) == 0:
                leafs += 1

        return nodes, leafs


def test_remove():
    tree = SimpleTree(None)
    node1 = TreeNode(1, None)
    node2 = TreeNode(2, None)
    node3 = TreeNode(3, None)
    node4 = TreeNode(4, None)
    node5 = TreeNode(5, None)
    tree.add(None, node1)
    tree.add(node1, node2)
    tree.add(node1, node3)
    tree.add(node2, node4)
    tree.add(node3, node5)

    tree.remove(node3)

    tree_test = SimpleTree(None)
    node1_test = TreeNode(1, None)
    node2_test = TreeNode(2, None)
    node4_test = TreeNode(4, None)
    tree_test.add(None, node1_test)
    tree_test.add(node1_test, node2_test)
    tree_test.add(node2_test, node4_test)

    for item, item_test in zip(tree, tree_test):
        assert item.value == item_test.value
        assert item.level == item_test.level


def test_find():
    tree = SimpleTree(None)
    node1 = TreeNode(1, None)
    node2 = TreeNode(2, None)
    node3 = TreeNode(3, None)
    node4 = TreeNode(4, None)
    node5 = TreeNode(1, None)
    tree.add(None, node1)
    tree.add(node1, node2)
    tree.add(node1, node3)
    tree.add(node2, node4)
    tree.add(node3, node5)

    assert tree.find(1) == [node1, node5]


def test_move():
    tree = SimpleTree(None)
    node1 = TreeNode(1, None)
    node2 = TreeNode(2, None)
    node3 = TreeNode(3, None)
    node4 = TreeNode(4, None)
    node5 = TreeNode(5, None)
    tree.add(None, node1)
    tree.add(node1, node2)
    tree.add(node1, node3)
    tree.add(node2, node4)
    tree.add(node3, node5)

    tree.move(node2, node3)

    tree_test = SimpleTree(None)
    node1_test = TreeNode(1, None)
    node2_test = TreeNode(2, None)
    node3_test = TreeNode(3, None)
    node4_test = TreeNode(4, None)
    node5_test = TreeNode(5, None)
    tree_test.add(None, node1_test)
    tree_test.add(node1_test, node2_test)
    tree_test.add(node2_test, node4_test)
    tree_test.add(node2_test, node3_test)
    tree_test.add(node3_test, node5_test)

    for item, item_test in zip(tree, tree_test):
        assert item.value == item_test.value
        assert item.level == item_test.level


def test_count():
    tree = SimpleTree(None)
    node1 = TreeNode(1, None)
    node2 = TreeNode(2, None)
    node3 = TreeNode(3, None)
    node4 = TreeNode(4, None)
    node5 = TreeNode(1, None)
    tree.add(None, node1)
    tree.add(node1, node2)
    tree.add(node1, node3)
    tree.add(node2, node4)
    tree.add(node3, node5)

    assert tree.count() == (5, 2)


if __name__ == '__main__':
    test_remove()
    test_find()
    test_move()
    test_count()
