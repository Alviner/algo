# -*- coding: utf-8 -*-
from enum import Enum

from stack import Stack


class TokenType(Enum):
    BRACKET = 'скобка'
    OPERATION = 'операция'
    NUMBER = 'число'


class ANode:
    def __init__(self, value):
        self.token_value = value
        self.token_type = self.__detect_tocken_type()

    def __detect_tocken_type(self):
        if self.token_value in ('+', '-', '/' '*'):
            return TokenType.OPERATION
        elif self.token_value in ('(', ')'):
            return TokenType.BRACKET
        return TokenType.NUMBER

    def __repr__(self):
        return f'[{self.token_type.value}, {self.token_value}]'


class AST(Stack):
    def __init__(self, expression: str):
        super(AST, self).__init__()
        self.expression = AST.__recover_brackets(expression)
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
        operations_first = ('*', '/')
        operations_second = ('+', '-')
        parts = []
        part = 0
        # раскладываем выражения в скобках в обратном порядке - с большой глубины к меньшей
        index = res.rfind('(')
        while index >= 0:
            parts.append({
                'index': f'p{part}{rec}',
                'part': res[index + 1:res.find(')', index)]
            })
            res = res[:index] + f'p{part}{rec}' + res[res.find(')', index) + 1:]
            part += 1
            index = res.rfind('(')
        # востанавливаем скобки в каждой из частей
        for part_item in parts:
            part_item['part'] = AST.__recover_brackets(part_item['part'])
        for operations in (operations_first, operations_second):
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
                    while res[i] not in operations_first + operations_second and i > 1:
                        i -= 1
                    is_last_i = False
                    # проверяем есть ли другие операторы в оставшейся строке
                    for k in operations_first + operations_second:
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
                    while res[j] not in operations_first + operations_second and j < len(res) - 1:
                        j += 1
                    is_last_j = False
                    # проверяем есть ли другие операторы в оставшейся строке
                    for k in operations_first + operations_second:
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
                        'index': f'p{part}{rec}',
                        'part': '(' + res[i: j] + ')'
                    })
                    res = res[:i] + f'p{part}{rec}' + res[j:]
                    part += 1
                    index = res.find(operation)
        # восстанавливаем строку по формату и части в обратном порядке
        for part_item in reversed(parts):
            res = res.replace(part_item['index'], part_item['part'])
        return res


def test_parser():
    ast = AST('7+3/25*(5-2)')
    test_ast = AST('(7+((3/25)*(5-2)))')
    assert ast.expression == test_ast.expression

    print(ast.stack)

    ast = AST('7+3*5-2')
    test_ast = AST('((7+(3*5))-2)')
    assert ast.expression == test_ast.expression
    print(ast.stack)

    ast = AST('(7+3)*(5-2)')
    test_ast = AST('((7+3)*(5-2))')
    assert ast.expression == test_ast.expression
    print(ast.stack)


if __name__ == '__main__':
    test_parser()
