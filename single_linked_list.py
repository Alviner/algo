#!/usr/bin/python



class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


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

    def remove(self, val, all = False):
        node = self.head
        while node is not None:
            if node.value == val:
                node.next = node.next.next
            node = node.next
        


if __name__ == '__main__':
    n1 = Node(12)
    n2 = Node(55)
    
    s_list = LinkedList()
    s_list.add_in_tail(n1)
    s_list.add_in_tail(n2)
    s_list.add_in_tail(Node(128))
    s_list.print_all_nodes()

    nf = s_list.find(55)
    if nf is not None:
        print(nf.value)

    s_list.remove(55)

    s_list.print_all_nodes()
