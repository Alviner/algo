# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'-> {self.value}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
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

    def remove(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None:
                    self.head = node.next
                    node.next.prev = None
                elif node.next is None:
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                return
            node = node.next

    def add_in_head(self, item):
        if self.head is not None:
            self.head.prev = item
        item.next = self.head
        item.prev = None
        self.head = item

    def add_in_pos(self, item, pos):
        assert pos < self.size()
        node = self.head
        k = 0
        while node is not None:
            if pos == k:
                if pos == 0:
                    self.add_in_head(item)
                elif pos == self.size() - 1:
                    self.add_in_tail(item)
                else:
                    item.next = node.next
                    item.prev = node
                    node.next.prev = item
                    node.next = item
            k += 1
            node = node.next

    def size(self):
        node = self.head
        res = 0
        while node is not None:
            res += 1
            node = node.next
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

    s_list.remove(1)
    s_list.remove(10)
    s_list.remove(3)
    s_list.remove(4)

    assert s_list.size() == s_list_test.size()

    node = s_list.head
    node_test = s_list_test.head
    while node is not None and node_test is not None:
        assert node.value == node_test.value
        node = node.next
        node_test = node_test.next


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


def add_head_test():
    s_list = LinkedList()
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(3))
    s_list.add_in_tail(Node(4))
    s_list.add_in_tail(Node(5))
    s_list.add_in_tail(Node(6))
    s_list.add_in_tail(Node(7))

    s_list_test = LinkedList()
    s_list_test.add_in_tail(Node(1))
    s_list_test.add_in_tail(Node(2))
    s_list_test.add_in_tail(Node(3))
    s_list_test.add_in_tail(Node(4))
    s_list_test.add_in_tail(Node(5))
    s_list_test.add_in_tail(Node(6))
    s_list_test.add_in_tail(Node(7))

    assert s_list.size() == s_list_test.size()

    node = s_list.head
    node_test = s_list_test.head
    while node is not None and node_test is not None:
        assert node.value == node_test.value
        node = node.next
        node_test = node_test.next


if __name__ == '__main__':
    remove_test()
    add_head_test()
    add_in_pos_test()
