# -*- coding: utf-8 -*-
import unittest
from single_linked_list import LinkedList, Node, merge_list


class TestLinkedList(unittest.TestCase):
    def test_remove(self):
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
        self.assertEqual(s_list.len(), s_list_test.len())

        node = s_list.head
        node_test = s_list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node.value)
            node = node.next
            node_test = node_test.next

    def test_mass_remove(self):
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
        self.assertEqual(s_list.len(), s_list_test.len())

        node = s_list.head
        node_test = s_list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node_test.value)
            node = node.next
            node_test = node_test.next

    def test_clear(self):
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

        self.assertEqual(s_list.len(), 0)

        self.assertIsNone(s_list.head, 'Проверяем, что голова пустая')
        self.assertIsNone(s_list.tail, 'Проверяем, что хвост пуст')

    def test_search(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(9))
        s_list.add_in_tail(Node(9))
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(9))
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(9))

        self.assertEqual(s_list.find(9), s_list.head)
        self.assertEqual(s_list.find(1), s_list.head.next.next)
        self.assertIsNone(s_list.find(120))

    def test_mass_search(self):
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

        self.assertEqual(len(s_list.find_all(9)), 4)
        self.assertEqual(len(s_list.find_all(1)), 5)
        self.assertEqual(len(s_list.find_all(128)), 2)

    def test_len(self):
        s_list = LinkedList()
        s_list.add_in_tail(Node(1))
        self.assertEqual(s_list.len(), 1)
        s_list.add_in_tail(Node(1))
        self.assertEqual(s_list.len(), 2)
        s_list.add_in_tail(Node(1))
        s_list.add_in_tail(Node(2))
        s_list.add_in_tail(Node(2))
        self.assertEqual(s_list.len(), 5)
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(128))
        s_list.add_in_tail(Node(9))
        s_list.add_in_tail(Node(9))
        s_list.add_in_tail(Node(1))
        self.assertEqual(s_list.len(), 10)
        s_list.add_in_tail(Node(9))
        s_list.add_in_tail(Node(1))
        self.assertEqual(s_list.len(), 12)
        s_list.add_in_tail(Node(9))
        self.assertEqual(s_list.len(), 13)

    def test_insert(self):
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

        self.assertEqual(s_list.len(), s_list_test.len())

        node = s_list.head
        node_test = s_list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node_test.value)
            node = node.next
            node_test = node_test.next

    def test_merge(self):
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

        self.assertEqual(s_list_merged.len(), s_list_test.len())

        node = s_list_merged.head
        node_test = s_list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node_test.value)
            node = node.next
            node_test = node_test.next



if __name__ == '__main__':
    unittest.main()
