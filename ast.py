# -*- coding: utf-8 -*-
from enum import Enum
import operator

from stack import Stack
from simple_tree import SimpleTree, TreeNode
import time

class TokenType(Enum):
    BRACKET = 'скобка'
    OPERATION = 'операция'
    NUMBER = 'число'


class ANode(TreeNode):
    def __init__(self, value, parent=None):
        super(ANode, self).__init__(value, parent)
        self.token_type = None
        self.expression = ''
        if value is not None:
            self.token_type = self.detect_tocken_type()

    def set(self, value):
        self.value = value
        self.token_type = self.detect_tocken_type()

    def detect_tocken_type(self):
        if self.value in ('+', '-', '/', '*'):
            return TokenType.OPERATION
        elif self.value in ('(', ')'):
            return TokenType.BRACKET
        else:
            return TokenType.NUMBER

    def __repr__(self):
        return '['+self.token_type.value+', '+self.value+']'


class AstStack(Stack):
    def __init__(self, expression: str):
        super(AstStack, self).__init__()
        self.expression = AstStack.__recover_brackets(expression)
        elem = ''
        for char in self.expression:
            if char in ('(', ')', '+', '-', '*', '/'):
                if len(elem) > 0:
                    self.push(ANode(elem))
                    elem = ''
                self.push(ANode(char))
            else:
                elem += char

    @staticmethod
    def __recover_brackets(expression: str, rec=0):
        res = expression
        operations_priority = (
            ('/', '*'),
            ('-', '+')
        )
        operations_list = [item for sublist in operations_priority for item in sublist]
        parts = []
        part = 0
        # раскладываем выражения в скобках в обратном порядке - с большой глубины к меньшей
        index = res.rfind('(')
        while index >= 0:
            parts.append({
                'index': 'p'+part+rec,
                'part': res[index + 1:res.find(')', index)]
            })
            res = res[:index] + 'p'+part+rec + res[res.find(')', index) + 1:]
            part += 1
            index = res.rfind('(')
        # востанавливаем скобки в каждой из частей
        for part_item in parts:
            part_item['part'] = AstStack.__recover_brackets(part_item['part'])
        for operations in operations_priority:
            sort_operations = []
            # определяем порядок операций слева направо
            for operation in operations:
                if res.find(operation) > 0:
                    sort_operations.append({'operation': operation, 'sort': res.find(operation)})
            operations = [x['operation'] for x in sorted(sort_operations, key=lambda k: k['sort'])]

            for operation in operations:
                index = res.find(operation)
                while index > 0:
                    i = index - 1
                    j = index + 1
                    # ищем слева следующий оператор
                    while res[i] not in operations_list and i > 1:
                        i -= 1
                    is_last_i = False
                    # проверяем есть ли другие операторы в оставшейся строке
                    for k in operations_list:
                        if res[:index].find(k) < 0:
                            is_last_i = True
                        else:
                            is_last_i = False
                            break
                    # если найденный оператор последний то скобку будем ставить в начале строки
                    if is_last_i:
                        i = 0
                    else:
                        # иначе ставим после найденного оператора
                        i += 1
                    # ищем слева следующий оператор
                    while res[j] not in operations_list and j < len(res) - 1:
                        j += 1
                    is_last_j = False
                    # проверяем есть ли другие операторы в оставшейся строке
                    for k in operations_list:
                        if res[j:].find(k) < 0:
                            is_last_j = True
                        else:
                            is_last_j = False
                            break
                    # если найденный оператор последний то скобку будем ставить в конце строки
                    if is_last_j:
                        j = len(res)
                    # заменяем в строке блок на строку формата p{номер_части}{уровень_рекурсии}
                    parts.append({
                        'index': 'p'+part+rec,
                        'part': '(' + res[i: j] + ')'
                    })
                    res = res[:i] + 'p'+part+rec + res[j:]
                    part += 1
                    index = res.find(operation)
        # восстанавливаем строку по формату и части в обратном порядке
        for part_item in reversed(parts):
            res = res.replace(part_item['index'], part_item['part'])
        return res


class Ast(SimpleTree):
    _op_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    def __init__(self, expression):
        node = ANode(None)
        super(Ast, self).__init__(node)
        self.token_list = AstStack(expression)
        while self.token_list.size() > 0:
            item = self.token_list.pop(0)
            if item.token_type is TokenType.BRACKET:
                if item.value == '(':
                    new_node = ANode(None)
                    self.add(node, new_node)
                    node = new_node
                else:
                    if node.parent is not None:
                        node = node.parent
                    else:
                        assert node == self.root
            if item.token_type is TokenType.NUMBER:
                node.set(item.value)
                node = node.parent
            if item.token_type is TokenType.OPERATION:
                node.set(item.value)
                new_node = ANode(None)
                self.add(node, new_node)
                node = new_node

    def interpret(self, node=None):
        if node is None:
            node = self.root
        if node != self.root or node.token_type is not TokenType.NUMBER:
            if node.child[0].token_type is TokenType.NUMBER and node.child[1].token_type is TokenType.NUMBER:
                node.expression = '('+node.child[0].value+node.value+node.child[1].value+')'
                node.set(Ast._op_map[node.value](float(node.child[0].value), float(node.child[1].value)))
                node.child = []
                if node.parent is not None:
                    self.interpret(node.parent)
            elif node.child[0].token_type is TokenType.OPERATION:
                self.interpret(node.child[0])
            elif node.child[1].token_type is TokenType.OPERATION:
                self.interpret(node.child[1])


def test_parser():
    ast_stack = AstStack('7+3/25*(5-2)')
    test_ast_stack = AstStack('(7+((3/25)*(5-2)))')
    assert ast_stack.expression == test_ast_stack.expression

    ast_stack = AstStack('7+3*5-2')
    test_ast_stack = AstStack('((7+(3*5))-2)')
    assert ast_stack.expression == test_ast_stack.expression

    ast_stack = AstStack('(7+3)*(5-2)')
    test_ast_stack = AstStack('((7+3)*(5-2))')
    assert ast_stack.expression == test_ast_stack.expression


def test_ast():
    ast = Ast('7+3/25*(5-2)')
    assert ast.root.value == '+'
    assert ast.root.child[0].value == '7'
    assert ast.root.child[1].value == '*'
    assert ast.root.child[1].child[0].value == '/'
    assert ast.root.child[1].child[0].child[0].value == '3'
    assert ast.root.child[1].child[0].child[1].value == '25'
    assert ast.root.child[1].child[1].value == '-'
    assert ast.root.child[1].child[1].child[0].value == '5'
    assert ast.root.child[1].child[1].child[1].value == '2'
    assert ast.count() == (9, 5)

    ast = Ast('(7+3)*(5-2)')
    assert ast.root.value == '*'
    assert ast.root.child[0].value == '+'
    assert ast.root.child[0].child[0].value == '7'
    assert ast.root.child[0].child[1].value == '3'
    assert ast.root.child[1].value == '-'
    assert ast.root.child[1].child[0].value == '5'
    assert ast.root.child[1].child[1].value == '2'
    assert ast.count() == (7, 4)

    ast = Ast('7+((3*5)-2)')
    assert ast.root.value == '+'
    assert ast.root.child[0].value == '7'
    assert ast.root.child[1].value == '-'
    assert ast.root.child[1].child[0].value == '*'
    assert ast.root.child[1].child[0].child[0].value == '3'
    assert ast.root.child[1].child[0].child[1].value == '5'
    assert ast.root.child[1].child[1].value == '2'
    assert ast.count() == (7, 4)


def test_translate():
    ast = Ast('5-20')
    ast.interpret()
    assert ast.root.value == 5 - 20

    ast = Ast('7+3/25*(5-2)')
    ast.interpret()
    assert ast.root.value == 7 + 3 / 25 * (5 - 2)

    ast = Ast('(7+3)*(5-2)')
    ast.interpret()
    assert ast.root.value == (7 + 3) * (5 - 2)

    ast = Ast('7+((3*5)-2)')
    ast.interpret()
    assert ast.root.value == 7 + ((3 * 5) - 2)


if __name__ == '__main__':
    start_time = time.time()
    test_parser()
    test_ast()
    test_translate()
    print("--- %s seconds ---" % (time.time() - start_time))