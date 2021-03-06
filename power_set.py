# -*- coding: utf-8 -*-

from hash_table import HashTable


def find_next_prime(n):
    return find_prime_in_range(n, 2*n)


def find_prime_in_range(a, b):
    for p in range(a, b):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            return p


class PowerSet(HashTable):
    def __init__(self, sz, stp):
        super(PowerSet, self).__init__(sz, stp)

    @staticmethod
    def __intersection(first, second):
        res = PowerSet(min(first.size, second.size), min(first.step, second.step))

        for item in first.slots:
            if item is not None:
                hash_key = second.find(item)
                if hash_key is not None:
                    if second.slots[hash_key] is item:
                        res.put(item)
        return res

    def put(self, value):
        hash_key = self.find(value)
        if hash_key is not None:
            self.slots[hash_key] = value

    def remove(self, value):
        hash_key = self.find(value)
        if hash_key is not None:
            self.slots[hash_key] = None

    def intersection(self, set):
        shorter_self = True if self.size < set.size else False

        if shorter_self:
            res = self.__intersection(self, set)
        else:
            res = self.__intersection(set, self)
        return res

    def union(self, set):
        res = PowerSet(find_next_prime(self.size + set.size + 1), self.step)

        for item in self.slots:
            if item is not None:
                res.put(item)

        for item in set.slots:
            if item is not None:
                res.put(item)

        return res

    def difference(self, set):
        res = PowerSet(self.size, self.step)

        for item in self.slots:
            if item is not None:
                hash_key = set.find(item)
                if hash_key is not None:
                    if set.slots[hash_key] is None:
                        res.put(item)

        return res

    def issubset(self, set):
        for item in self.slots:
            if item is not None:
                hash_key = set.find(item)
                if set.slots[hash_key] is not item:
                    return False
        return True


def test_put():
    ps = PowerSet(17, 3)
    ps.put('1')
    ps.put('2')
    ps.put('3')
    ps.put('1')

    ps_test = set()
    ps_test.add('1')
    ps_test.add('2')
    ps_test.add('3')
    ps_test.add('1')

    length = 0
    for i in ps.slots:
        if i is not None:
            assert i in ps_test
            length += 1
    assert len(ps_test) == length


def test_remove():
    ps = PowerSet(17, 3)
    ps.put('1')
    ps.put('2')
    ps.put('3')
    ps.put('1')

    ps.remove('3')
    ps.remove('2')

    ps_test = ['1', '2', '3', '1']
    ps_test = set(ps_test)

    ps_test.remove('3')
    ps_test.remove('2')

    length = 0
    for i in ps.slots:
        if i is not None:
            assert i in ps_test
            length += 1
    assert len(ps_test) == length


def test_intersection():
    ps_first = PowerSet(17, 3)
    ps_secont = PowerSet(17, 3)

    ps_first.put('1')
    ps_first.put('2')
    ps_first.put('3')
    ps_first.put('4')

    ps_secont.put('3')
    ps_secont.put('4')
    ps_secont.put('5')
    ps_secont.put('6')
    ps_secont.put('7')

    ps = ps_first.intersection(ps_secont)

    ps_test_first = ['1', '2', '3', '4']
    ps_test_first = set(ps_test_first)

    ps_test_second = ['3', '4', '5', '6', '7']
    ps_test_second = set(ps_test_second)

    ps_test = ps_test_first.intersection(ps_test_second)
    length = 0
    for i in ps.slots:
        if i is not None:
            assert i in ps_test
            length += 1
    assert len(ps_test) == length


def test_union():
    ps_first = PowerSet(17, 3)
    ps_secont = PowerSet(17, 3)

    ps_first.put('1')
    ps_first.put('2')
    ps_first.put('3')
    ps_first.put('4')

    ps_secont.put('3')
    ps_secont.put('4')
    ps_secont.put('5')
    ps_secont.put('6')
    ps_secont.put('7')

    ps = ps_first.union(ps_secont)

    ps_test_first = ['1', '2', '3', '4']
    ps_test_first = set(ps_test_first)

    ps_test_second = ['3', '4', '5', '6', '7']
    ps_test_second = set(ps_test_second)

    ps_test = ps_test_first.union(ps_test_second)
    length = 0
    for i in ps.slots:
        if i is not None:
            assert i in ps_test
            length += 1
    assert len(ps_test) == length


def test_difference():
    ps_first = PowerSet(17, 3)
    ps_secont = PowerSet(17, 3)

    ps_first.put('1')
    ps_first.put('2')
    ps_first.put('3')
    ps_first.put('4')

    ps_secont.put('3')
    ps_secont.put('4')
    ps_secont.put('5')
    ps_secont.put('6')
    ps_secont.put('7')

    ps = ps_first.difference(ps_secont)

    ps_test_first = ['1', '2', '3', '4']
    ps_test_first = set(ps_test_first)

    ps_test_second = ['3', '4', '5', '6', '7']
    ps_test_second = set(ps_test_second)

    ps_test = ps_test_first.difference(ps_test_second)

    length = 0
    for i in ps.slots:
        if i is not None:
            assert i in ps_test
            length += 1
    assert len(ps_test) == length


def test_issubset():
    ps_first = PowerSet(17, 3)
    ps_secont = PowerSet(17, 3)

    ps_first.put('3')
    ps_first.put('4')

    ps_secont.put('3')
    ps_secont.put('4')
    ps_secont.put('5')
    ps_secont.put('6')
    ps_secont.put('7')

    ps = ps_first.issubset(ps_secont)

    ps_test_first = ['3', '4']
    ps_test_first = set(ps_test_first)

    ps_test_second = ['3', '4', '5', '6', '7']
    ps_test_second = set(ps_test_second)

    ps_test = ps_test_first.issubset(ps_test_second)

    assert ps == ps_test


if __name__ == '__main__':
    test_put()
    test_remove()
    test_intersection()
    test_union()
    test_difference()
    test_issubset()
