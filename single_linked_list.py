# -*- coding: utf-8 -*-

from functools import wraps


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __repr__(self):
        return f'-> {self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next
        print()

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def remove(self, val, mass=False):
        while True:
            node = self.head
            if node is not None:
                if node.value == val:
                    self.head = node.next
                    if not mass:
                        return
                else:
                    break

        node = self.head
        while node is not None:
            go_next = True  # need take next node

            if node.next is not None:

                if node.next.value == val:
                    if node.next == self.tail:
                        self.tail = node
                    node.next = node.next.next
                    go_next = False  # dont need take next one cuz shift
                    if not mass:
                        return
            node = node.next if go_next else node

    def find_all(self, val):
        node = self.head
        res = []
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def clear(self):
        self.__init__()

    def size(self):
        res = 0
        node = self.head
        while node is not None:
            res += 1
            node = node.next
        return res

    def add_in_pos(self, item, pos):
        assert pos < self.size(), 'pos is less than size'
        if pos == 0:
            item.next = self.head
            self.head = item
            return
        node = self.head
        size = 0
        while node is not None:
            if size == pos:
                if node == self.tail:
                    self.tail = item
                item.next = node.next
                node.next = item
                return
            node = node.next
            size += 1


def merge_list(list_one: LinkedList, list_two: LinkedList):
    assert list_one.size() == list_two.size(), 'need equal size'
    res = LinkedList()

    node_one = list_one.head
    node_two = list_two.head
    while node_one is not None and node_two is not None:
        res.add_in_tail(Node(
            node_one.value + node_two.value
        ))
        node_one = node_one.next
        node_two = node_two.next
    return res


def print_task(func):
    @wraps(func)
    def wrapped():
        print('{:#^30}'.format(func.__name__))
        func()
        print('{:#^30}'.format(''))
    return wrapped


@print_task
def t11():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))

    s_list.print_all_nodes()

    s_list.remove(1)
    print('single remove 1')
    s_list.print_all_nodes()

    print('single remove 2')
    s_list.remove(2)
    s_list.print_all_nodes()

    print('single remove 9')
    s_list.remove(9)
    s_list.print_all_nodes()


@print_task
def t12():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))

    s_list.print_all_nodes()

    s_list.remove(1, mass=True)
    print('mass remove 1')
    s_list.print_all_nodes()

    print('mass remove 9')
    s_list.remove(9, mass=True)
    s_list.print_all_nodes()


@print_task
def t13():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))

    s_list.print_all_nodes()

    s_list.clear()
    s_list.print_all_nodes()


@print_task
def t14():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))

    s_list.print_all_nodes()

    print(s_list.find_all(9))
    print(s_list.find_all(128))
    print(s_list.find_all(2))


@print_task
def t15():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    print(s_list.size())
    s_list.add_in_tail(Node(1))
    print(s_list.size())
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    print(s_list.size())
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    print(s_list.size())
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    print(s_list.size())
    s_list.add_in_tail(Node(9))
    print(s_list.size())


@print_task
def t16():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(9))

    s_list.print_all_nodes()

    s_list.add_in_pos(Node(-11), 0)
    s_list.add_in_pos(Node(-10), 0)
    s_list.add_in_pos(Node(-9), 0)
    s_list.add_in_pos(Node(-1), 6)
    s_list.add_in_pos(Node(-2), 2)
    s_list.add_in_pos(Node(-3), 8)
    s_list.add_in_pos(Node(-111), s_list.size() - 1)
    s_list.print_all_nodes()


@print_task
def t17():
    s_list_one = LinkedList()
    s_list_one.add_in_tail(Node(1))
    s_list_one.add_in_tail(Node(2))
    s_list_one.add_in_tail(Node(3))
    s_list_one.add_in_tail(Node(4))
    s_list_one.add_in_tail(Node(5))
    s_list_one.add_in_tail(Node(6))
    s_list_one.add_in_tail(Node(7))
    s_list_one.add_in_tail(Node(8))
    s_list_one.add_in_tail(Node(9))
    s_list_one.add_in_tail(Node(10))
    s_list_one.add_in_tail(Node(11))
    s_list_one.add_in_tail(Node(12))
    s_list_one.add_in_tail(Node(13))

    s_list_one.print_all_nodes()

    s_list_two = LinkedList()
    s_list_two.add_in_tail(Node(13))
    s_list_two.add_in_tail(Node(12))
    s_list_two.add_in_tail(Node(11))
    s_list_two.add_in_tail(Node(10))
    s_list_two.add_in_tail(Node(9))
    s_list_two.add_in_tail(Node(8))
    s_list_two.add_in_tail(Node(7))
    s_list_two.add_in_tail(Node(6))
    s_list_two.add_in_tail(Node(5))
    s_list_two.add_in_tail(Node(4))
    s_list_two.add_in_tail(Node(3))
    s_list_two.add_in_tail(Node(2))
    s_list_two.add_in_tail(Node(1))

    s_list_two.print_all_nodes()

    s_list_merged = merge_list(s_list_two, s_list_one)
    s_list_merged.print_all_nodes()


if __name__ == '__main__':
    t11()
    t12()
    t13()
    t14()
    t15()
    t16()
    t17()
