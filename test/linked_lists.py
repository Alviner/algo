# -*- coding: utf-8 -*-
import unittest
from single_linked_list import LinkedList, Node, merge_list


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
        self.list_test = LinkedList()
        
    def test_remove(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(10))
        self.list.add_in_tail(Node(3))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(4))
        self.list.add_in_tail(Node(1))
        
        self.list_test.add_in_tail(Node(2))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(2))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(1))

        self.list.delete(1)
        self.list.delete(10)
        self.list.delete(3)
        self.list.delete(4)
        self.assertEqual(self.list.len(), self.list_test.len())

        node = self.list.head
        node_test = self.list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node.value)
            node = node.next
            node_test = node_test.next

    def test_mass_remove(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))

        self.list_test.add_in_tail(Node(2))
        self.list_test.add_in_tail(Node(2))
        self.list_test.add_in_tail(Node(128))
        self.list_test.add_in_tail(Node(128))

        self.list.delete(1, all=True)
        self.list.delete(9, all=True)
        self.assertEqual(self.list.len(), self.list_test.len())

        node = self.list.head
        node_test = self.list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node_test.value)
            node = node.next
            node_test = node_test.next

    def test_clear(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))

        self.list.clean()

        self.assertEqual(self.list.len(), 0)

        self.assertIsNone(self.list.head, 'Проверяем, что голова пустая')
        self.assertIsNone(self.list.tail, 'Проверяем, что хвост пуст')

    def test_search(self):
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))

        self.assertEqual(self.list.find(9), self.list.head)
        self.assertEqual(self.list.find(1), self.list.head.next.next)
        self.assertIsNone(self.list.find(120))

    def test_mass_search(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))

        self.assertEqual(len(self.list.find_all(9)), 4)
        self.assertEqual(len(self.list.find_all(1)), 5)
        self.assertEqual(len(self.list.find_all(128)), 2)

    def test_len(self):
        self.list.add_in_tail(Node(1))
        self.assertEqual(self.list.len(), 1)
        self.list.add_in_tail(Node(1))
        self.assertEqual(self.list.len(), 2)
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(2))
        self.assertEqual(self.list.len(), 5)
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.assertEqual(self.list.len(), 10)
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.assertEqual(self.list.len(), 12)
        self.list.add_in_tail(Node(9))
        self.assertEqual(self.list.len(), 13)

    def test_insert(self):
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(2))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(128))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))
        self.list.add_in_tail(Node(1))
        self.list.add_in_tail(Node(9))

        self.list_test.add_in_tail(Node(-9))
        self.list_test.add_in_tail(Node(-10))
        self.list_test.add_in_tail(Node(-11))
        self.list_test.add_in_tail(Node(-2))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(2))
        self.list_test.add_in_tail(Node(-1))
        self.list_test.add_in_tail(Node(-3))
        self.list_test.add_in_tail(Node(2))
        self.list_test.add_in_tail(Node(128))
        self.list_test.add_in_tail(Node(128))
        self.list_test.add_in_tail(Node(9))
        self.list_test.add_in_tail(Node(9))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(9))
        self.list_test.add_in_tail(Node(1))
        self.list_test.add_in_tail(Node(9))
        self.list_test.add_in_tail(Node(-111))

        self.list.insert(None, Node(-11))
        self.list.insert(None, Node(-10))
        self.list.insert(None, Node(-9))
        self.list.insert(self.list.head.next.next.next.next.next.next, Node(-1))
        self.list.insert(self.list.head.next.next, Node(-2))
        self.list.insert(self.list.head.next.next.next.next.next.next.next.next, Node(-3))
        self.list.insert(self.list.tail, Node(-111))

        self.assertEqual(self.list.len(), self.list_test.len())

        node = self.list.head
        node_test = self.list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node_test.value)
            node = node.next
            node_test = node_test.next

        self.list.clean()
        self.list_test.clean()

        node = Node(2)

        self.list.insert(None, node)

        self.assertEqual(self.list.head, node)
        self.assertEqual(self.list.tail, node)

        self.list_test.add_in_tail(node)
        self.assertEqual(self.list_test.head, node)
        self.assertEqual(self.list_test.tail, node)

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

        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))
        self.list_test.add_in_tail(Node(14))

        self.assertEqual(s_list_merged.len(), self.list_test.len())

        node = s_list_merged.head
        node_test = self.list_test.head
        while node is not None and node_test is not None:
            self.assertEqual(node.value, node_test.value)
            node = node.next
            node_test = node_test.next


if __name__ == '__main__':
    unittest.main()
