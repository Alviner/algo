# -*- coding: utf-8 -*-


class AssociativeArray:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def _hash_fun(self, key):
        res = 0
        for i in key:
            res += ord(i)
        return res % self.size

    def put(self, key, value):
        hash_key = self._seek_slot(key)
        if hash_key is not None:
            self.slots[hash_key] = key
            self.values[hash_key] = value

    def is_key(self, key):
        return True if self.find(key) is not None else False

    def get(self, key):
        hash_key = self.find(key)
        if hash_key is not None:
            return self.values[hash_key]
        else:
            return None

    def _seek_slot(self, key):
        hash_key = self._hash_fun(key)
        limit = self.step * (self.size // self.step)
        while self.slots[hash_key] is not None and limit > 0:
            if self.slots[hash_key] is key:
                break
            hash_key = (hash_key + self.step) % self.size
            limit -= 1
        if limit == 0:
            return None
        return hash_key

    def find(self, key):
        hash_key = self._hash_fun(key)
        limit = self.step * (self.size // self.step)
        while self.slots[hash_key] is not None and limit > 0:
            if self.slots[hash_key] is key:
                return hash_key
            hash_key = (hash_key + self.step) % self.size
            limit -= 1
        return None


def test_hash_func():
    hs = AssociativeArray(17, 3)
    print()
    assert hs._hash_fun('1') == 15


def test_put():
    hs = AssociativeArray(17, 3)

    hs.put('12', 1)
    hs.put('21', 2)

    hs_test_slots = [None] * 17
    hs_test_values = [None] * 17
    hs_test_slots[14] = '12'
    hs_test_values[14] = 1
    hs_test_slots[0] = '21'
    hs_test_values[0] = 2
    assert hs.size == len(hs_test_slots) == len(hs_test_values)

    for i, i_v, t_i, t_i_v in zip(hs.slots, hs.values, hs_test_slots, hs_test_values):
        assert i == t_i
        assert  i_v == t_i_v


def test_is_key():
    hs = AssociativeArray(17, 3)

    hs.put('12', 1)
    hs.put('21', 2)

    assert hs.is_key('12')
    assert hs.is_key('21')
    assert not hs.is_key('1')


def test_get():
    hs = AssociativeArray(17, 3)

    hs.put('12', 1)
    hs.put('21', 2)

    assert hs.get('12') == 1
    assert hs.get('21') == 2
    assert hs.get('1') is None


def test_seek():
    hs = AssociativeArray(17, 3)

    hs.put('12', 1)
    hs.put('21', 2)

    assert hs._seek_slot('12') == 14
    assert hs._seek_slot('21') == 0


if __name__ == '__main__':
    test_hash_func()
    test_put()
    test_seek()
    test_is_key()
    test_get()
