# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __repr__(self):
        return f'-> {self.value}'


class NodeStr(Node):
    def __init__(self, v):
        super(NodeStr, self).__init__(v)

    def __eq__(self, other):
        return self.value.strip() == other.value.strip()

    def __lt__(self, other):
        return self.value.strip() < other.value.strip()

    def __gt__(self, other):
        return self.value.strip() > other.value.strip()

    def __le__(self, other):
        return self.value.strip() <= other.value.strip()

    def __ge__(self, other):
        return self.value.strip() >= other.value.strip()


class OrderedList:
    asc = 'asc'
    desc = 'desc'

    def __init__(self):
        self.head = None
        self.tail = None
        self.order = None

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next
        print()

    def add(self, item):  # O(n) ~ O(1)
        node = self.head
        go_next = True
        if self.order == OrderedList.asc:
            while node is not None and go_next:
                if node <= item:
                    node = node.next
                else:
                    go_next = False
            if node is None:
                self.add_in_tail(item)
            elif node.prev is None:
                self.add_in_head(item)
            else:
                item.next = node
                item.prev = node.prev

                node.prev.next = item
                node.prev = item
        elif self.order == OrderedList.desc:
            while node is not None and go_next:
                if node >= item:
                    node = node.next
                else:
                    go_next = False
            if node is None:
                self.add_in_tail(item)
            elif node.prev is None:
                self.add_in_head(item)
            else:
                item.next = node
                item.prev = node.prev

                node.prev.next = item
                node.prev = item
        else:
            self.add_in_tail(item)

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
            сработает прерывание и сложность операции упадет до O(1), O(n) будет в самом худшем случае,
            когда искомый элемент находится в хвосте, в среднем будет лучше чем O(n)
        """
        node = self.head
        temp = Node(item)
        go_next = True
        if self.order == OrderedList.asc:
            while node is not None and go_next:
                if node >= temp:
                    go_next = False
                else:
                    node = node.next
            if node is not None:
                return node if node == temp else None
        elif self.order == OrderedList.desc:
            while node is not None and go_next:
                if node <= temp:
                    go_next = False
                else:
                    node = node.next
            if node is not None:
                return node if node == temp else None
        else:
            while node is not None:
                if node == temp:
                    return node
                node = node.next
        return None

    def size(self):
        node = self.head
        res = 0
        while node is not None:
            res += 1
            node = node.next
        return res


def test_order_numbers():
    ol = OrderedList()
    ol.order = OrderedList.asc
    ol.add(Node(1))
    ol.add(Node(7))
    ol.add(Node(2))
    ol.add(Node(5))
    ol.add(Node(4))
    ol.add(Node(3))
    ol.add(Node(0))
    ol_test = OrderedList()
    ol_test.add_in_tail(Node(0))
    ol_test.add_in_tail(Node(1))
    ol_test.add_in_tail(Node(2))
    ol_test.add_in_tail(Node(3))
    ol_test.add_in_tail(Node(4))
    ol_test.add_in_tail(Node(5))
    ol_test.add_in_tail(Node(7))

    assert ol.size() == ol_test.size()

    node = ol.head
    node_test = ol_test.head
    while node is not None and node_test is not None:
        assert node == node_test
        node = node.next
        node_test = node_test.next

    ol = OrderedList()
    ol.order = OrderedList.desc
    ol.add(Node(1))
    ol.add(Node(7))
    ol.add(Node(2))
    ol.add(Node(5))
    ol.add(Node(4))
    ol.add(Node(3))
    ol.add(Node(0))
    ol_test = OrderedList()
    ol_test.add_in_tail(Node(7))
    ol_test.add_in_tail(Node(5))
    ol_test.add_in_tail(Node(4))
    ol_test.add_in_tail(Node(3))
    ol_test.add_in_tail(Node(2))
    ol_test.add_in_tail(Node(1))
    ol_test.add_in_tail(Node(0))

    assert ol.size() == ol_test.size()

    node = ol.head
    node_test = ol_test.head
    while node is not None and node_test is not None:
        assert node == node_test
        node = node.next
        node_test = node_test.next


def test_order_string():
    ol = OrderedList()
    ol.order = OrderedList.asc
    ol.add(NodeStr(' 1'))
    ol.add(NodeStr('7 '))
    ol.add(NodeStr(' 2'))
    ol.add(NodeStr('5 '))
    ol.add(NodeStr(' 4'))
    ol.add(NodeStr('3 '))
    ol.add(NodeStr(' 0'))
    ol_test = OrderedList()
    ol_test.add_in_tail(NodeStr('0'))
    ol_test.add_in_tail(NodeStr('1'))
    ol_test.add_in_tail(NodeStr('2'))
    ol_test.add_in_tail(NodeStr('3'))
    ol_test.add_in_tail(NodeStr('4'))
    ol_test.add_in_tail(NodeStr('5'))
    ol_test.add_in_tail(NodeStr('7'))

    assert ol.size() == ol_test.size()

    node = ol.head
    node_test = ol_test.head
    while node is not None and node_test is not None:
        assert node == node_test
        node = node.next
        node_test = node_test.next

    ol = OrderedList()
    ol.order = OrderedList.desc
    ol.add(NodeStr('  1 '))
    ol.add(NodeStr('7 '))
    ol.add(NodeStr('   2'))
    ol.add(NodeStr('5   '))
    ol.add(NodeStr(' 4'))
    ol.add(NodeStr('3  '))
    ol.add(NodeStr('   0'))
    ol_test = OrderedList()
    ol_test.add_in_tail(NodeStr('  7'))
    ol_test.add_in_tail(NodeStr('5 '))
    ol_test.add_in_tail(NodeStr(' 4'))
    ol_test.add_in_tail(NodeStr('3 '))
    ol_test.add_in_tail(NodeStr(' 2'))
    ol_test.add_in_tail(NodeStr('1 '))
    ol_test.add_in_tail(NodeStr(' 0'))

    assert ol.size() == ol_test.size()

    node = ol.head
    node_test = ol_test.head
    while node is not None and node_test is not None:
        assert node == node_test
        node = node.next
        node_test = node_test.next


def test_find():
    ol = OrderedList()
    ol.order = OrderedList.asc
    ol.add(Node(1))
    ol.add(Node(7))
    ol.add(Node(2))
    ol.add(Node(5))
    ol.add(Node(4))
    ol.add(Node(3))
    ol.add(Node(0))

    assert ol.find(5) == Node(5)
    assert ol.find(-1) is None


if __name__ == '__main__':
    test_order_numbers()
    test_order_string()
    test_find()