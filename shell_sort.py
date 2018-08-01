# -*- coding: utf-8 -*-

from sort import pred_insertion_sort


def is_sorted(items: list):
    for i in range(0, len(items) - 2):
        if items[i] > items[i + 1]:
            return False
    return True


def shell_sort(items: list):
    if len(items) < 2:
        return items

    res = items.copy()

    i = 0
    knuth_list = []
    knuth_list.append(1)
    while knuth_list[i] < len(res):
        i += 1
        knuth_list.append(3 * knuth_list[i - 1] + 1)
    for it in reversed(knuth_list[:-1]):
        if is_sorted(res):
            break
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