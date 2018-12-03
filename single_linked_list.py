# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None

    def __repr__(self):
        return self.value


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


def merge_list(list_one, list_two):
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