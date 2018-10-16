# -*- coding: utf-8 -*-

import random

from binary_tree import BinaryTree
from stack import Stack
from queue import Queue
from termcolor import colored


class BinaryWeldedTreeHalf(BinaryTree):
    def __init__(self, depth: int, colors: int, is_reversed: bool, colors_list: list):
        super(BinaryWeldedTreeHalf, self).__init__(root=None)
        self.depth = depth
        self.colors = colors
        self.reversed = is_reversed
        color = 0
        node = None
        stack = Stack()
        queue = Queue()
        stack.push(self.add(colors_list[color]))
        for i in range(self.depth):
            while stack.size() > 0 or queue.size() % 2 != 0:
                if not node:
                    node = stack.pop(0)
                if node.left_child and node.right_child:
                    node = stack.pop(0)
                choosen_colors = [node.value]
                if node.right_child:
                    choosen_colors.append(node.right_child.value)
                if node.left_child:
                    choosen_colors.append(node.left_child.value)
                color = random.choice([c for c in range(self.colors) if colors_list[c] not in list(set(choosen_colors))])
                queue.enqueue(self.add(colors_list[color], node))
            while queue.size() > 0:
                stack.push(queue.dequeue())

    def __repr__(self, node=None):
        ret = ''
        if node is None:
            node = self.root
        tab = '            '
        if node.left_child:
            ret += self.__repr__(node.left_child)
        slide = 4 * self.depth - node.level if self.reversed else node.level
        node_ret = f"{tab * (slide - 1)}{colored('--', node.value)}{colored(node.__repr__(), node.value)}\n"

        # ret += ' ' * len(node_ret) + colored('--', node.rvalue)
        ret += node_ret
        # ret += ' ' * len(node_ret)
        if node.right_child:
            ret += self.__repr__(node.right_child)
        return ret


class BinaryWeldedTree:
    colors_list = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta']

    def __init__(self, depth: int, colors: int):
        assert colors <= len(self.colors_list)
        self.depth = depth
        self.colors = colors
        self.left_side = BinaryWeldedTreeHalf(depth=self.depth, colors=colors,
                                              is_reversed=False, colors_list=self.colors_list[:self.colors])
        self.right_side = BinaryWeldedTreeHalf(depth=self.depth, colors=colors,
                                               is_reversed=True, colors_list=self.colors_list[:self.colors])

        left_queue = Queue()
        right_queue = Queue()
        self.parts_connections = {}

        for node in self.left_side:
            if not node.left_child and not node.right_child:
                left_queue.enqueue({'node': node, 'connections': 2})
                self.parts_connections[node] = []

        for node in self.right_side:
            if not node.left_child and not node.right_child:
                right_queue.enqueue({'node': node, 'connections': 2})
                self.parts_connections[node] = []

        while left_queue.size() > 0:
            left_connection = left_queue.dequeue()
            right_connection = right_queue.dequeue()

            while right_connection['node'] in self.parts_connections[left_connection['node']]:
                right_queue.enqueue(right_connection)
                right_connection = right_queue.dequeue()

            self.parts_connections[left_connection['node']].append(right_connection['node'])
            self.parts_connections[right_connection['node']].append(left_connection['node'])
            left_connection['connections'] -= 1
            right_connection['connections'] -= 1

            if left_connection['connections'] > 0:
                left_queue.enqueue(left_connection)
            if right_connection['connections'] > 0:
                right_queue.enqueue(right_connection)
        self._merge_colors_parts()

    def __repr__(self):
        right_ret = self.right_side.__repr__()
        left_ret = self.left_side.__repr__()
        ret = ''
        max_len = 0
        for left_line in left_ret.splitlines():
            max_len = len(left_line) if max_len < len(left_line) else max_len
        new_left_lines = []
        for left_line in left_ret.splitlines():
            new_left_lines.append(left_line.ljust(max_len, ' '))
        for it, (left_line, right_line) in enumerate(zip(new_left_lines, right_ret.splitlines())):
            ret += f'{left_line}{right_line}\n'
        return ret

    def _merge_colors_parts(self):
        pass
        queue = Queue()
        for node in self.left_side:
            if not node.left_child and not node.right_child:
                queue.enqueue(node)
        while queue.size() > 0:
            left_node = queue.dequeue()
            choosen_parts_colors = [left_node.value]
            for node in self.parts_connections[left_node]:
                choosen_colors = list(set(choosen_parts_colors + [x.value for x in self.parts_connections[node]]))
                if node.value in choosen_parts_colors + choosen_colors:
                    node.value = self.colors_list[
                        random.choice([c for c in range(self.colors)
                                       if self.colors_list[c] not in choosen_parts_colors + choosen_colors])
                    ]
                    choosen_parts_colors.append(node.value)


if __name__ == '__main__':
    tree = BinaryWeldedTree(2, 4)
    print(tree)
    print(tree.parts_connections)
