# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __repr__(self):
        return f'<Node({self.value})>'


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
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        res = []
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        prev_node = None
        node = self.head
        while node is not None:
            if node.value == val:
                if node == self.tail:
                    self.tail = prev_node
                if prev_node is None:
                    self.head = node.next
                else:
                    prev_node.next = node.next
                if not all:
                    return
            else:
                prev_node = node
            node = node.next

    def clean(self):
        self.__init__()

    def len(self):
        res = 0
        node = self.head
        while node is not None:
            res += 1
            node = node.next
        return res

    def insert(self, after_node, new_node):
        if after_node is None:
            new_node.next = self.head
            self.head = new_node
            return
        node = self.head
        size = 0
        while node is not None:
            if node == after_node:
                if node == self.tail:
                    self.tail = new_node
                new_node.next = node.next
                node.next = new_node
                return
            node = node.next
            size += 1


def merge_list(list_one: LinkedList, list_two: LinkedList):
    assert list_one.len() == list_two.len(), 'need equal size'
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

    s_list.delete(1)
    s_list.delete(10)
    s_list.delete(3)
    s_list.delete(4)
    assert s_list.len() == s_list_test.len()

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

    s_list.delete(1, all=True)
    s_list.delete(9, all=True)
    assert s_list.len() == s_list_test.len()

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

    s_list.clean()

    assert s_list.len() == 0

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
    assert s_list.len() == 1
    s_list.add_in_tail(Node(1))
    assert s_list.len() == 2
    s_list.add_in_tail(Node(1))
    s_list.add_in_tail(Node(2))
    s_list.add_in_tail(Node(2))
    assert s_list.len() == 5
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(128))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    assert s_list.len() == 10
    s_list.add_in_tail(Node(9))
    s_list.add_in_tail(Node(1))
    assert s_list.len() == 12
    s_list.add_in_tail(Node(9))
    assert s_list.len() == 13


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

    s_list.insert(None, Node(-11))
    s_list.insert(None, Node(-10))
    s_list.insert(None, Node(-9))
    s_list.insert(s_list.head.next.next.next.next.next.next, Node(-1))
    s_list.insert(s_list.head.next.next, Node(-2))
    s_list.insert(s_list.head.next.next.next.next.next.next.next.next, Node(-3))
    s_list.insert(s_list.tail, Node(-111))

    assert s_list.len() == s_list_test.len()

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

    assert s_list_merged.len() == s_list_test.len()

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
