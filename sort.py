# -*- coding: utf-8 -*-


def insertion_sort(items: list):
    if len(items) < 2:
        return items
    i = 1
    res = items.copy()
    while i < len(res):
        j = 0
        while j < i:
            if res[i] >= res[j]:
                j += 1
            else:
                res.insert(j, res[i])
                del res[i + 1]
                break
        i += 1
    return res


def selection_sort(items: list):
    if len(items) < 2:
        return items
    i = 0
    res = items.copy()
    while i < len(res):
        j = i
        min_index = j
        while j < len(res):
            if res[min_index] > res[j]:
                min_index = j
            j += 1
        temp = res[i]
        res[i] = res[min_index]
        res[min_index] = temp
        i += 1
    return res


def bubble_sort(items: list):
    if len(items) < 2:
        return items
    res = items.copy()
    it = 1
    while it > 0:
        it = 0
        for i in range(len(res) - 1):
            if res[i] > res[i + 1]:
                temp = res[i]
                res[i] = res[i + 1]
                res[i + 1] = temp
                it += 1
    return res


def pred_insertion_sort(items: list, step=1):
    if len(items) < 2:
        return items
    res = items.copy()
    it = step

    while it >= 0:
        for i in range(step):
            res[step - i - 1::step] = insertion_sort(res[step - i - 1::step])
        it -= 1
    return res


def test_sort():
    test_sort = [1, 2, 3, 4]

    sort = [4, 3, 1, 2]

    sort = insertion_sort(sort)

    for i, i_test in zip(sort, test_sort):
        assert i == i_test

    sort = [4, 3, 1, 2]

    sort = selection_sort(sort)

    for i, i_test in zip(sort, test_sort):
        assert i == i_test

    sort = [4, 3, 1, 2]

    sort = bubble_sort(sort)

    for i, i_test in zip(sort, test_sort):
        assert i == i_test

    sort = [7, 6, 5, 4, 3, 2, 1]
    test_sort = [1, 3, 2, 4, 6, 5, 7]

    sort = pred_insertion_sort(sort, 3)
    for i, i_test in zip(sort, test_sort):
        assert i == i_test

    sort = [7, 6, 5, 4, 3, 2, 1]
    test_sort = [1, 2, 3, 4, 5, 6, 7]

    sort = pred_insertion_sort(sort)

    for i, i_test in zip(sort, test_sort):
        assert i == i_test


if __name__ == '__main__':
    test_sort()