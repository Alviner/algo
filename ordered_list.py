# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class OrderedList:

    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.value > v2.value:
            res = 1
        elif v1.value == v2.value:
            res = 0
        else:
            res = -1
        return res

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next
        print()

    def add(self, item):  # O(n) ~ O(1)

        node = self.head
        go_next = True

        while node is not None and go_next:
            if (self.compare(node, item) <= 0 and self.__ascending) or \
                    (self.compare(node, item) >= 0 and not self.__ascending):
                node = node.next
            else:
                go_next = False

        if node is None:  # Дошли до конца списка
            self.add_in_tail(item)
        elif node.prev is None:  # Находимся на первом элементе
            self.add_in_head(item)
        else:  # Вставка в середину
            item.next = node
            item.prev = node.prev

            node.prev.next = item
            node.prev = item

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, item):
        if self.tail is None:
            self.tail = item
            item.prev = None
            item.next = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

    def find(self, item):  # O(n) ~ O(1)
        """
            В случае сортированного списка, когда найден заведомо больший или меньший элемент
            сработает прерывание и сложность операции упадет даже до O(1), O(n) будет в самом худшем случае,
            когда искомый элемент находится в хвосте, в среднем будет лучше чем O(n)
        """
        node = self.head
        temp = Node(item)
        go_next = True
        while node is not None and go_next:
            if (self.compare(node, temp) >= 0 and self.__ascending) or (
                    self.compare(node, temp) <= 0 and not self.__ascending):
                go_next = False
            else:
                node = node.next
        if node is not None:
            return node if self.compare(node, temp) == 0 else None
        return None

    def clean(self):
        self.__init__(self.__ascending)

    def delete(self, value):
        node = self.find(value)
        if node is not None:
            if node.prev is None:
                self.head = node.next
                if node.next is not None:
                    node.next.prev = None
                else:
                    self.tail = None
            elif node.next is None:
                self.tail = node.prev
                node.prev.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

    def len(self):
        return len(self.get_all())

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1_str, v2_str):
        v1 = v1_str.value.split()
        v2 = v2_str.value.split()
        if v1 > v2:
            res = 1
        elif v1 == v2:
            res = 0
        else:
            res = -1
        return res
