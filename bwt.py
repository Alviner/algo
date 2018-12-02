# -*- coding: utf-8 -*-

import random
from enum import Enum
from queue import Queue
from termcolor import colored


class Color(Enum):
    red = 'red'
    grey = 'grey'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'
    magenta = 'magenta'


class Node:
    def __init__(self, parent=None, value=None):
        self.parent = parent
        self.left_connection = None
        self.right_connection = None
        self.value = value

    def set_right_connection(self, node, color: Color):
        node.parent = self
        self.right_connection = Connection(node, color)

        return self.right_connection

    def set_left_connection(self, node, color: Color):
        node.parent = self
        self.left_connection = Connection(node, color)

        return self.left_connection

    def __repr__(self):
        return f'Node({self.value})'


class BorderNode:
    def __init__(self, parent_left: Node, parent_right: Node):
        self.parent_left = parent_left
        self.parent_right = parent_right

    def __repr__(self):
        return ''


class Connection:
    def __init__(self, node, color: Color):
        self.node = node
        self.color = color

    def __repr__(self):
        return self.node.__repr__()

    def get_used_colors(self):
        colors = [self.color]
        if self.node.left_connection:
            colors.append(self.node.left_connection.color)
        if self.node.right_connection:
            colors.append(self.node.right_connection.color)
        return set(colors)


class BinaryTree:
    def __init__(self, root: Connection = None, reversed=False, depth: int=0):
        self.root = root
        self.reversed = reversed
        self.depth = depth

    def __iter__(self, connection=None):
        if connection is None:
            connection = self.root
        yield connection
        if connection.node.left_connection:
            for item in self.__iter__(connection.node.left_connection):
                yield item
        if connection.node.right_connection:
            for item in self.__iter__(connection.node.right_connection):
                yield item

    def __repr__(self, connection=None, level=1):
        ret = ''
        if connection is None:
            connection = self.root
        tab = '            '
        node = connection.node
        slide = 4 * self.depth - level if self.reversed else level
        conn_ret = ''
        if isinstance(node, Node):
            if node.left_connection:
                ret += self.__repr__(node.left_connection, level + 1)
            if node.parent:
                conn_ret += colored(f' {node.parent.value} ', connection.color.value)
        else:
            if self.reversed:
                if node.parent_left:
                    conn_ret += colored(f' {node.parent_left.value} ', connection.color.value)
            else:
                if node.parent_right:
                    conn_ret += colored(f' {node.parent_right.value} ', connection.color.value)
        conn_ret = conn_ret + connection.__repr__() if not self.reversed else connection.__repr__() + conn_ret
        node_ret = f"{tab * (slide - 1)}{conn_ret}\n"

        ret += node_ret
        if isinstance(node, Node):
            if node.right_connection:
                ret += self.__repr__(node.right_connection, level + 1)
        return ret


class BinaryWeldedTree:
    def __init__(self, depth: int, colors_list: list):
        self.depth = depth
        self.colors = set(colors_list)
        count = 0
        self.right_tree = BinaryTree(Connection(Node(None, count), random.choice(colors_list)), True, self.depth)
        count += 1
        self.left_tree = BinaryTree(Connection(Node(None, count), random.choice(colors_list)), False, self.depth)
        count += 1

        queue_right = Queue()
        queue_left = Queue()

        queue_right.enqueue(self.right_tree.root)
        queue_left.enqueue(self.left_tree.root)
        for i in range(depth):
            left_splice = []
            right_splice = []
            while queue_left.size() > 0:
                connection = queue_left.dequeue()
                node = connection.node
                left_splice.append(node.set_right_connection(Node(node, count),
                                                             random.choice(
                                                                 list(self.colors.difference(
                                                                     connection.get_used_colors()))
                                                             ))
                                   )
                count += 1
                left_splice.append(node.set_left_connection(Node(node, count),
                                                            random.choice(
                                                                list(self.colors.difference(
                                                                    connection.get_used_colors()))
                                                            ))
                                   )
                count += 1
            while queue_right.size() > 0:
                connection = queue_right.dequeue()
                node = connection.node
                right_splice.append(node.set_right_connection(Node(node, count),
                                                              random.choice(
                                                                  list(self.colors.difference(
                                                                      connection.get_used_colors()))
                                                              ))
                                    )
                count += 1
                right_splice.append(node.set_left_connection(Node(node, count),
                                                             random.choice(
                                                                 list(self.colors.difference(
                                                                     connection.get_used_colors()))
                                                             ))
                                    )
                count += 1
            while len(left_splice) > 0:
                queue_left.enqueue(left_splice.pop())
            while len(right_splice) > 0:
                queue_right.enqueue(right_splice.pop())

        left_queue = Queue()
        right_queue = Queue()
        self.bordered = {}

        for connection in self.left_tree:
            if not (connection.node.left_connection and connection.node.right_connection):
                left_queue.enqueue({'connection': connection, 'counts': 2})
                self.bordered[connection] = []

        for connection in self.right_tree:
            if not (connection.node.left_connection and connection.node.right_connection):
                right_queue.enqueue({'connection': connection, 'counts': 2})
                self.bordered[connection] = []

        while left_queue.size() > 0 and right_queue.size() > 0:
            left_connection = left_queue.dequeue()
            right_connection = right_queue.dequeue()

            while right_connection['connection'] in self.bordered[left_connection['connection']]:
                right_queue.enqueue(right_connection)
                right_connection = right_queue.dequeue()

            self.bordered[left_connection['connection']].append(right_connection['connection'])
            self.bordered[right_connection['connection']].append(left_connection['connection'])

            border_node = BorderNode(left_connection['connection'].node, right_connection['connection'].node)

            color = random.choice(
                list(self.colors.difference(
                    left_connection['connection'].get_used_colors().union(right_connection['connection'].get_used_colors())))
            )
            if left_connection['connection'].node.right_connection is None:
                left_connection['connection'].node.right_connection = Connection(
                    border_node,
                    color
                )

                right_connection['connection'].node.right_connection = Connection(
                    border_node,
                    color
                )
            else:
                left_connection['connection'].node.left_connection = Connection(
                    border_node,
                    color
                )

                right_connection['connection'].node.left_connection = Connection(
                    border_node,
                    color
                )

            left_connection['counts'] -= 1
            right_connection['counts'] -= 1

            if left_connection['counts'] > 0:
                left_queue.enqueue(left_connection)
            if right_connection['counts'] > 0:
                right_queue.enqueue(right_connection)

    def __repr__(self):
        right_ret = self.right_tree.__repr__()
        left_ret = self.left_tree.__repr__()
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


if __name__ == '__main__':
    colors = list(Color)
    btw = BinaryWeldedTree(2, colors[:5])
    print(btw)
    print(btw.bordered)
