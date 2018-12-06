# -*- coding: utf-8 -*-

import unittest
import random
from dynarray import DynArray


class TestDynArray(unittest.TestCase):
    def setUp(self):
        self.array = DynArray()

    def is_equal(self, base_arr, tested_arr):
        for i, it in enumerate(base_arr):
            self.assertEqual(tested_arr[i], it)
        self.assertEqual(len(base_arr), len(tested_arr))

    def test_insert_fixed_buffer(self):
        self.array.insert(0, 1)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array.capacity, 16)

        self.array.insert(0, 2)
        self.assertEqual(self.array[0], 2)
        self.assertEqual(self.array.capacity, 16)

        self.array.insert(1, 3)
        self.assertEqual(self.array[1], 3)
        self.assertEqual(self.array.capacity, 16)

        self.array.insert(3, 4)
        self.assertEqual(self.array[3], 4)
        self.assertEqual(self.array.capacity, 16)

    def test_insert_change_buffer(self):
        insert_arr = [
            3,
            2,
            4,
            6,
            6,
            5,
            1,
            6,
            7,
            8,
            12,
            76,
            14,
            54,
            65,
            123,
        ]
        created_arr = []
        for item in insert_arr:
            it = random.randint(0, self.array.count)
            self.array.insert(it, item)
            self.assertEqual(self.array[it], item)
            self.assertEqual(self.array.capacity, 16)
            created_arr.insert(it, item)
            self.is_equal(created_arr, self.array)
        self.array.insert(0, -1)
        created_arr.insert(0, -1)
        self.assertEqual(self.array[len(self.array) - 1], created_arr[len(created_arr) - 1])
        self.assertEqual(self.array.capacity, 16 * 2)

        self.is_equal(created_arr, self.array)

        with self.assertRaises(IndexError):
            self.array.insert(120, 2341)
        with self.assertRaises(IndexError):
            self.array.insert(-1, 1)

    def test_delete(self):
        insert_arr = [
            3,
            2,
            4,
            6,
            6,
            5,
            1,
            6,
            7,
            8,
            12,
            76,
            14,
            54,
            65,
            123
        ]
        created_arr = []
        for item in insert_arr:
            it = random.randint(0, self.array.count)
            self.array.insert(it, item)
            self.assertEqual(self.array[it], item)
            self.assertEqual(self.array.capacity, 16)
            created_arr.insert(it, item)

        self.array.insert(0, 124)
        created_arr.insert(0, 124)
        self.is_equal(created_arr, self.array)
        self.assertEqual(self.array.capacity, 16 * 2)

        self.array.delete(0)
        del created_arr[0]
        self.is_equal(created_arr, self.array)
        self.assertEqual(self.array.capacity, int(16 * 2 * 2 / 3))

        while self.array.count > 0:
            i = random.randint(0, self.array.count - 1)
            del created_arr[i]
            self.array.delete(i)
            self.is_equal(created_arr, self.array)
            self.assertEqual(len(created_arr), self.array.count)

        with self.assertRaises(IndexError):
            self.array.delete(120)
        with self.assertRaises(IndexError):
            self.array.delete(-1)
