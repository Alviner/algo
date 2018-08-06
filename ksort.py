# -*- coding: utf-8 -*-

import random
import string
import time


class Ksort():
    def __init__(self, len=8):
        self.alph = string.ascii_lowercase[0:len]
        self.values = [{'count': 0, 'value': self._unhash(x)} for x in range(len * 100)]

    def _hash(self, item: str):
        a, m, n = item
        a = self.alph.index(a)
        return int(f'{a}{m}{n}')

    def _unhash(self, index: int):
        hash_value = f'{str(index):0>3}'
        return self.alph[int(hash_value[0])] + hash_value[1:]

    def append(self, item: str):
        hash_value = self._hash(item)
        self.values[hash_value]['count'] += 1

    def sort(self):
        res = []
        for i, item in enumerate(self.values):
            while item['count'] > 0:
                item['count'] -= 1
                res.append(item['value'])
        return res


def test_ksort():
    items = []
    alph = string.ascii_lowercase[0:8]
    ksort = Ksort()

    for i in range(1000000):
        value = f'{alph[random.randint(0, 7)]}{random.randint(0, 9)}{random.randint(0, 9)}'
        items.append(value)
        ksort.append(value)

    start = time.time()
    ksort_items = ksort.sort()
    print(f'Ksort time {time.time() - start}')

    start = time.time()
    items.sort()
    print(f'Sort time {time.time() - start}')

    assert ksort_items == items


if __name__ == '__main__':
    test_ksort()
