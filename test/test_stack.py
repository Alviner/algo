# -*- coding: utf-8 -*-

import unittest
import random
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()
        self.test_stack = []

    def compare(self, first: Stack, second: list):
        for i, j in zip(first, second):
            self.assertEqual(i, j)
        self.assertEqual(first.size(), len(second))

    def test_push(self):
        test_items = [random.randint(-100, 100) for x in range(100)]

        for i in test_items:
            self.stack.push(i)
            self.test_stack.append(i)
            self.compare(self.stack, self.test_stack)

    def test_peak(self):
        self.assertIsNone(self.stack.peak())
        test_items = [random.randint(-100, 100) for x in range(100)]

        for i in test_items:
            self.stack.push(i)
            self.test_stack.append(i)
            self.assertEqual(self.stack.peak(), self.test_stack[0])

    def test_pop(self):
        self.assertIsNone(self.stack.pop())
        test_items = [random.randint(-100, 100) for x in range(100)]

        for i in test_items:
            self.stack.push(i)
            self.test_stack.append(i)
            if self.stack.size() == 0 and len(self.test_stack) == 0:
                self.assertIsNone(self.stack.pop())
                self.assertIsNone(self.test_stack.pop())
            else:
                self.assertEqual(self.stack.pop(), self.test_stack.pop())
