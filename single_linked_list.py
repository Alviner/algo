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

    def remove_with_tmp(self, val, mass=False):
        prev_node = None
        node = self.head
        while node is not None:
            if node.value == val:
                if prev_node is None:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if not mass:
                    return
            else:
                prev_node = node
            node = node.next

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


def remove_test():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(10))
    s_list.add_in_tail(Node(3))
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(4))
    s_list.add_in_tail(Node(1))

    s_list_test = LinkedList()
    s_list_test.add_in_tail(Node(2))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(2))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(1))

    s_list.remove_with_tmp(1)
    s_list.remove_with_tmp(10)
    s_list.remove_with_tmp(3)
    s_list.remove_with_tmp(4)
    assert s_list.size() == s_list_test.size()

    node = s_list.head
    node_test = s_list_test.head
    while node is not None and node_test is not None:
        assert node.value == node_test.value
        node = node.next
        node_test = node_test.next


def mass_remove_test():
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

    s_list_test = LinkedList()
    s_list_test.add_in_tail(Node(2))
    s_list_test.add_in_tail(Node(2))
    s_list_test.add_in_tail(Node(128))
    s_list_test.add_in_tail(Node(128))

    s_list.remove_with_tmp(1, mass=True)
    s_list.remove_with_tmp(9, mass=True)
    assert s_list.size() == s_list_test.size()

    node = s_list.head
    node_test = s_list_test.head
    while node is not None and node_test is not None:
        assert node.value == node_test.value
        node = node.next
        node_test = node_test.next


def clear_test():
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

    s_list.clear()

    assert s_list.size() == 0

    assert s_list.head is None
    assert s_list.tail is None


def mass_search_test():
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

    assert len(s_list.find_all(9)) == 4
    assert len(s_list.find_all(1)) == 5
    assert len(s_list.find_all(128)) == 2


def size_test():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    assert s_list.size() == 1
    s_list.add_in_tail(Node(1))
    assert s_list.size() == 2
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    assert s_list.size() == 5
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    assert s_list.size() == 10
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    assert s_list.size() == 12
    s_list.add_in_tail(Node(9))
    assert s_list.size() == 13


def add_in_pos_test():
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

    s_list_test = LinkedList()
    s_list_test.add_in_tail(Node(-9))
    s_list_test.add_in_tail(Node(-10))
    s_list_test.add_in_tail(Node(-11))
    s_list_test.add_in_tail(Node(-2))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(2))
    s_list_test.add_in_tail(Node(-1))
    s_list_test.add_in_tail(Node(-3))
    s_list_test.add_in_tail(Node(2))
    s_list_test.add_in_tail(Node(128))
    s_list_test.add_in_tail(Node(128))
    s_list_test.add_in_tail(Node(9))
    s_list_test.add_in_tail(Node(9))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(9))
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(9))
    s_list_test.add_in_tail(Node(-111))

    s_list.add_in_pos(Node(-11), 0)
    s_list.add_in_pos(Node(-10), 0)
    s_list.add_in_pos(Node(-9), 0)
    s_list.add_in_pos(Node(-1), 6)
    s_list.add_in_pos(Node(-2), 2)
    s_list.add_in_pos(Node(-3), 8)
    s_list.add_in_pos(Node(-111), s_list.size() - 1)

    assert s_list.size() == s_list_test.size()

    node = s_list.head
    node_test = s_list_test.head
    while node is not None and node_test is not None:
        assert node.value == node_test.value
        node = node.next
        node_test = node_test.next


def merge_test():
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

    s_list_merged = merge_list(s_list_two, s_list_one)

    s_list_test = LinkedList()

    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))
    s_list_test.add_in_tail(Node(14))

    assert s_list_merged.size() == s_list_test.size()

    node = s_list_merged.head
    node_test = s_list_test.head
    while node is not None and node_test is not None:
        assert node.value == node_test.value
        node = node.next
        node_test = node_test.next


if __name__ == '__main__':
    remove_test()
    mass_remove_test()
    clear_test()
    mass_search_test()
    size_test()
    add_in_pos_test()
    merge_test()
