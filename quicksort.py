# -*- coding: utf-8 -*-

import random
from shell_sort import shell_sort, is_sorted
import time


def _swap(items: list, first_index: int, second_index: int):
    items[first_index], items[second_index] = items[second_index], items[first_index]


def _part_quicksort(items: list, left: int, right: int):
    first_index = left
    second_index = right

    while first_index != second_index:
        while items[first_index] < items[right] and first_index < second_index:
            first_index += 1
        while items[second_index] >= items[right] and first_index < second_index:
            second_index -= 1

        if first_index != second_index:
            _swap(items, first_index, second_index)
    _swap(items, right, first_index)
    return first_index, items[first_index: right + 1].count(items[first_index])


def quicksort(items, left: int, right: int):
    if right - left >= 1:
        sep, pivots = _part_quicksort(items, left, right)
        quicksort(items, left, sep - 1)
        if sep + pivots < right + 1:
            quicksort(items, sep + 1, right)


def test_part_quicksort():
    items = [
        7,
        1,
        6,
        2,
        5,
        3,
        4
    ]
    sep, pivots = _part_quicksort(items, 0, len(items) - 1)

    test_before = []
    test_after = items.copy()

    test_before.sort()
    test_after.sort()

    before = items[:sep].copy()
    after = items[sep:].copy()
    before.sort()
    after.sort()

    for i, i_test in zip(before, test_before):
        assert i, i_test

    for i, i_test in zip(after, test_after):
        assert i, i_test


def test_quicksort():
    items = []

    for i in range(0, 10000):
        items.append(random.randint(1, 100))

    quicksort(items, 0, len(items) - 1)
    assert is_sorted(items)


def test_shell_quicksort():
    quicksort_items = []
    # random.seed(42)
    for i in range(0, 10000):
        quicksort_items.append(random.randint(1, 100))
    shellsort_items = quicksort_items.copy()

    start_quicksort = time.time()
    quicksort(quicksort_items, 0, len(quicksort_items) - 1)
    end_quicksort = time.time()

    start_shellsort = time.time()
    shell_sort(shellsort_items)
    end_shellsort = time.time()

    assert is_sorted(quicksort_items)
    assert is_sorted(shellsort_items)

    print(f'Quicksort time: {end_quicksort - start_quicksort}')
    print(f'Shellsort time: {end_shellsort - start_shellsort}')


if __name__ == '__main__':
    # test_part_quicksort()
    # test_quicksort()
    test_shell_quicksort()
