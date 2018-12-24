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
        limit = self.step * (self.size // self.step)
        while self.slots[hash_key] is not None and limit > 0:
            if self.slots[hash_key] is value:
                return hash_key
            hash_key = (hash_key + self.step) % self.size
            limit -= 1
        if limit == 0:
            return None
        return hash_key

    def put(self, value):
        hash_key = self.seek_slot(value)
        if hash_key is not None:
            self.slots[hash_key] = value

    def find(self, value):
        index = self.seek_slot(value)
        if index is not None:
            if self.slots[index] is not None:
                return index
        return None
