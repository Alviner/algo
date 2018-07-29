# -*- coding: utf-8 -*-


def _swap(items: list, first_index: int, second_index: int):
    items[first_index], items[second_index] = items[second_index], items[first_index]


def _get_pivot(items: list):
    first_index = 0
    second_index = len(items) - 1
    res = items.copy()

    medium = int((first_index + second_index) / 2)
    if res[medium] < res[first_index]:
        _swap(res, first_index, medium)
    if res[second_index] < res[first_index]:
        _swap(res, first_index, second_index)
    if res[second_index] < res[medium]:
        _swap(res, second_index, medium)
    _swap(res, second_index, medium)

    return res[second_index]


def _part_quicksort(items: list, pivot):
    start = 0
    end = len(items) - 1
    first_index = start
    second_index = end

    while True:
        while items[first_index] <= pivot and first_index < second_index:
            first_index += 1
        while items[second_index] > pivot and first_index < second_index:
            second_index -= 1

        if first_index == end:
            if items[first_index] > pivot:
                return end
            else:
                return end + 1

        if first_index == second_index:
            break
        _swap(items, first_index, second_index)
    return first_index


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
    pivot = -1
    sep = _part_quicksort(items, pivot)

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

    # __________________________________________
    pivot = 8
    sep = _part_quicksort(items, pivot)

    test_before = items.copy()
    test_after = []

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

    # __________________________________________
    pivot = 1
    sep = _part_quicksort(items, pivot)

    test_before = [1]
    test_after = items.copy()

    for item in test_before:
        if item in test_after:
            del test_before[test_before.index(item)]

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

    # __________________________________________
    pivot = 2
    sep = _part_quicksort(items, pivot)

    test_before = [1, 2]
    test_after = items.copy()

    for item in test_before:
        if item in test_after:
            del test_before[test_before.index(item)]

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

    # __________________________________________
    pivot = 3
    sep = _part_quicksort(items, pivot)

    test_before = [1, 2, 3]
    test_after = items.copy()

    for item in test_before:
        if item in test_after:
            del test_before[test_before.index(item)]

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

    # __________________________________________
    pivot = 4
    sep = _part_quicksort(items, pivot)

    test_before = [1, 2, 3, 4]
    test_after = items.copy()

    for item in test_before:
        if item in test_after:
            del test_before[test_before.index(item)]

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

    # __________________________________________
    pivot = 5
    sep = _part_quicksort(items, pivot)

    test_before = [1, 2, 3, 4, 5]
    test_after = items.copy()

    for item in test_before:
        if item in test_after:
            del test_before[test_before.index(item)]

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

    # __________________________________________
    pivot = 6
    sep = _part_quicksort(items, pivot)

    test_before = [1, 2, 3, 4, 5, 6]
    test_after = items.copy()

    for item in test_before:
        if item in test_after:
            del test_before[test_before.index(item)]

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

    # __________________________________________
    pivot = 7
    sep = _part_quicksort(items, pivot)

    test_before = [1, 2, 3, 4, 5, 6, 7]
    test_after = items.copy()

    for item in test_before:
        if item in test_after:
            del test_before[test_before.index(item)]

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


if __name__ == '__main__':
    test_part_quicksort()
