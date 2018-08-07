# -*- coding: utf-8 -*-

import random
from quicksort import quicksort


def binary_search(items, value):
    if len(items) == 0:
        return False
    if len(items) == 1:
        if items[0] == value:
            return True
        else:
            return False

    medium = int(len(items) / 2)

    if items[medium] > value:
        return binary_search(items[:medium], value)
    elif items[medium] == value:
        return True
    else:
        return binary_search(items[medium:], value)


def test_binary_search():
    items = []

    for i in range(1000):
        items.append(random.randint(0, 999))

    quicksort(items, 0, len(items) - 1)

    for i in range(100):
        assert binary_search(items, random.choice(items))
    assert not binary_search(items, -1)


if __name__ == '__main__':
    test_binary_search()
