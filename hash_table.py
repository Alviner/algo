# -*- coding: utf-8 -*-


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        res = 0
        for i in value:
            res += ord(i)
        return res % self.size

    def seek_slot(self, value):
        hash_key = self.hash_fun(value)

        while self.slots[hash_key] is not None:
            if self.slots[hash_key] is value:
                break
            hash_key = (hash_key + self.step) % self.size
        return hash_key

    def put(self, value):
        self.slots[self.seek_slot(value)] = value

    def find(self, value):
        hash_key = self.hash_fun(value)
        while self.slots[hash_key] is not None:
            if self.slots[hash_key] is value:
                return hash_key
            hash_key = (hash_key + self.step) % self.size
        return None


def test_hash_func():
    hs = HashTable(17, 3)
    print()
    assert hs.hash_fun('1') == 15


def test_put():
    hs = HashTable(17, 3)

    hs.put('12')
    hs.put('21')

    hs_test = [None] * 17
    hs_test[14] = '12'
    hs_test[0] = '21'
    assert hs.size == len(hs_test)

    for i, i_test in zip(hs.slots, hs_test):
        assert i == i_test


def test_seek():
    hs = HashTable(17, 3)

    hs.put('12')
    hs.put('21')

    assert hs.seek_slot('12') == 14
    assert hs.seek_slot('21') == 0


if __name__ == '__main__':
    test_hash_func()
    test_put()
    test_seek()