# -*- coding: utf-8 -*-
"""
Мера сложности разнится из-за особенностей структуры списка.
К примеру: append и pop() работает за O(1), работа в данных методах ведется с хвостом списка,
а вот insert и pop(0) уже работает за O(n), т.к. работа уже идет с головой списка
"""


class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):  # O(1)
        return self.queue.append(item)

    def addTail(self, item):  # O(n)
        return self.queue.insert(0, item)

    def removeFront(self):  # O(1)
        res = None
        if len(self.queue) > 0:
            res = self.queue.pop()
        return res

    def removeTail(self):  # O(n)
        res = None
        if len(self.queue) > 0:
            res = self.queue.pop(0)
        return res

    def size(self):
        return len(self.queue)


def check_palindrome(check_string):
    deq = Deque()
    is_palindlome = True

    check_string = check_string.lower()
    check_string = check_string.replace(' ', '')

    for i in range(int(len(check_string) / 2)):
        deq.addFront(check_string[i])
        deq.addTail(check_string[-(i + 1)])

    while deq.size() > 0 and is_palindlome:
        if deq.removeFront() != deq.removeTail():
            is_palindlome = False

    if deq.size() == 0 and is_palindlome:
        return True
    return False


def test_palindrome():
    check_string = 'А роза упала на лапу Азора'
    assert check_palindrome(check_string)
    check_string = 'Аргентина манит негра'
    assert check_palindrome(check_string)
    check_string = 'Я иду с мечем судия'
    assert check_palindrome(check_string)
    check_string = 'Sum summus mus'
    assert check_palindrome(check_string)
    check_string = 'Saippuakivikauppias'
    assert check_palindrome(check_string)
    check_string = '223'
    assert not check_palindrome(check_string)
