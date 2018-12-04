# -*- coding: utf-8 -*-
import unittest
from doubly_linked_list import LinkedList2, Node


class TestLinkedList2(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList2()

    def test_find(self):
        node_list = [
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
        ]
        for node in node_list:
            self.list.add_in_tail(node)
        self.assertEqual(self.list.find(1), node_list[0])
        self.assertEqual(self.list.find(2), node_list[3])
        self.assertEqual(self.list.find(9), node_list[5])
        self.assertIsNone(self.list.find(123))

    def test_find_all(self):
        node_list = [
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
            Node(10)
        ]
        for node in node_list:
            self.list.add_in_tail(node)
        self.assertEqual(self.list.find_all(1), node_list[0:3])
        self.assertEqual(self.list.find_all(2), node_list[3:5])
        self.assertEqual(self.list.find_all(9), node_list[5:7])
        self.assertEqual(self.list.find_all(10), node_list[-1:])
        self.assertEqual(self.list.find_all(3123), [])

    def test_delete(self):
        node_list = [
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
            Node(10)
        ]

        self.list.add_in_tail(node_list[0])
        self.list.delete(1)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)


        for node in node_list:
            self.list.add_in_tail(node)
        self.list.delete(1)
        self.assertEqual(self.list.head, node_list[1])
        self.assertIsNone(self.list.head.prev)

        self.list.delete(10)
        self.assertEqual(self.list.tail, node_list[-2])
        self.assertIsNone(self.list.tail.next)

        self.list.delete(2)
        self.assertEqual(self.list.head.next.next, node_list[4])
        self.assertIsNotNone(self.list.head.next.next.prev)
        self.assertIsNotNone(self.list.head.next.next.next)

    def test_delete_all(self):
        node_list = [
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
            Node(10)
        ]
        for node in node_list:
            self.list.add_in_tail(node)
        self.list.delete(1, True)
        self.assertEqual(self.list.head, node_list[3])
        self.assertIsNone(self.list.head.prev)

        self.list.delete(10, True)
        self.assertEqual(self.list.tail, node_list[-2])
        self.assertIsNone(self.list.tail.next)

        self.list.delete(2, True)
        self.assertEqual(self.list.head, node_list[-3])
        self.assertIsNone(self.list.head.prev)

    def test_insert(self):
        node_list = [
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
            Node(10)
        ]

        insert_node = [
            Node(2),
            Node(5),
            Node(7),
            Node(1),
            Node(10),
        ]
        for node in node_list:
            self.list.add_in_tail(node)

        self.list.insert(None, insert_node[0])
        self.assertEqual(self.list.head, insert_node[0])
        self.assertIsNone(self.list.head.prev)

        self.list.insert(node_list[-1], insert_node[1])
        self.assertEqual(self.list.tail, insert_node[1])
        self.assertIsNone(self.list.tail.next)

        self.list.insert(node_list[2], insert_node[2])
        self.assertEqual(self.list.head.next.next.next.next, insert_node[2])
        self.assertIsNotNone(self.list.head.next.next.next.next.next)
        self.assertIsNotNone(self.list.head.next.next.next.next.prev)
        self.assertEqual(self.list.head.next.next.next.next.prev, node_list[2])
        self.assertEqual(self.list.head.next.next.next.next.next, node_list[3])

    def test_add_in_head(self):
        insert_node = [
            Node(2),
            Node(5),
            Node(7),
            Node(1),
            Node(10),
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
            Node(10)
        ]

        for node in insert_node:
            prev_head = self.list.head
            self.list.add_in_head(node)
            self.assertEqual(self.list.head, node)
            self.assertIsNone(self.list.head.prev)
            self.assertEqual(self.list.head.next, prev_head)
            if prev_head is not None:
                self.assertEqual(prev_head.prev, self.list.head)

    def test_clean(self):
        node_list = [
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
            Node(10)
        ]

        for node in node_list:
            self.list.add_in_tail(node)

        self.list.clean()
        self.assertEqual(self.list.len(), 0)
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_len(self):
        node_list = [
            Node(1),
            Node(1),
            Node(1),
            Node(2),
            Node(2),
            Node(9),
            Node(9),
            Node(10)
        ]

        insert_node = [
            Node(2),
            Node(5),
            Node(7),
            Node(1),
            Node(10),
        ]
        for node in node_list:
            self.list.add_in_tail(node)

        self.assertEqual(self.list.len(), len(node_list))

        for i, node in enumerate(insert_node):
            self.list.add_in_head(node)
            self.assertEqual(self.list.len(), len(node_list) + i + 1)
