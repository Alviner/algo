# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def clean(self):
        self.__init__()

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, item):
        if self.tail is None:
            self.tail = item
            item.prev = None
            item.next = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None:
                    self.head = node.next
                    if node.next is not None:
                        node.next.prev = None
                    else:
                        self.tail = None
                elif node.next is None:
                    self.tail = node.prev
                    node.prev.next = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def insert(self, after_node, new_node):
        if after_node is None:
            if self.head is None:
                self.add_in_head(new_node)
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            return
        node = self.head
        while node is not None:
            if node == after_node:
                if node == self.tail:
                    self.add_in_tail(new_node)
                    return
                new_node.next = node.next
                new_node.prev = node
                node.next.prev = new_node
                node.next = new_node
                return
            node = node.next

    def len(self):
        node = self.head
        res = 0
        while node is not None:
            res += 1
            node = node.next
        return res
