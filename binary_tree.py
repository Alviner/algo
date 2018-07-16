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

    def remove(self, value):
        node, is_exist, position = self.find(value)
        if is_exist:
            if self.value == node.value:
                parent_node = self
            else:
                parent_node = node.parent

            if node.left_child is None and node.right_child is None:
                if value < parent_node.value:
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None
                return

            if node.left_child is not None and node.right_child is None:
                if node.left_child.value < parent_node.value:
                    parent_node.left_child = node.left_child
                else:
                    parent_node.right_child = node.left_child
                return

            if node.right_child is not None and node.left_child is None:
                if node.value <= parent_node.value:
                    parent_node.left_child = node.right_child
                else:
                    parent_node.right_child = node.right_child
                return

            if node.left_child is not None and node.right_child is not None:
                min_node = self.find_minimum(node)
                node.value = min_node.value
                min_node.parent.left_child = None
                return

    def find_minimum(self, node):
        if node.right_child is not None:
            node = node.right_child
        else:
            return node

        if node.left_child is not None:
            return self.find_minimum(node=node.left_child)
        else:
            return node

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


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __iter__(self):
        return self.root.__iter__()

    def __repr__(self):
        return self.root.__repr__()

    def add(self, other):
        if self.root is None:
            self.root = TreeNode(other)
        else:
            self.root.add(other)

    def find(self, value):
        if self.root is not None:
            return self.root.find(value)

    def remove(self, value):
        if self.root is not None:
            self.root.remove(value)


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(8)
    tree.add(4)
    tree.add(12)
    tree.add(2)
    tree.add(6)
    print(tree)

    tree.remove(8)
    print(tree)
