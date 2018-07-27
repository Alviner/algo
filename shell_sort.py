# -*- coding: utf-8 -*-

from sort import pred_insertion_sort


def knuth_set(i):
    if i == 0:
        return 1
    else:
        return 3 * knuth_set(i - 1) + 1


def shell_sort(items: list):
    if len(items) < 2:
        return items

    res = items.copy()

    i = 0
    knuth_list = []
    knuth_list.append(knuth_set(i))
    while knuth_list[i] < len(res):
        i += 1
        knuth_list.append(knuth_set(i))

    for it in reversed(knuth_list):
        res = pred_insertion_sort(res, it)
    return res


def test_shell():
    sort = [7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1]
    test_sort = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]

    sort = shell_sort(sort)

    for i, i_test in zip(sort, test_sort):
        assert i == i_test


if __name__ == '__main__':
    test_shell()