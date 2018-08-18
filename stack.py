# -*- coding: utf-8 -*-

# while stack.size() > 0:
#     print(stack.pop())
#     print(stack.pop())
# Отработает успешно, выведет весь стек, однако если количество элементов нечетно, то в конце выведет еще None


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self, index=None):  # O(n) когда работаем с головой списка, O(1) когда работали с хвостом
        if self.size() == 0:
            return None
        return self.stack.pop(index)

    def push(self, item):  # O(n)
        return self.stack.append(item)

    def peak(self):
        if self.size() == 0:
            return None
        return self.stack[0]

    def size(self):
        return len(self.stack)


def check_balansed(bracket_string):
    right_brackets = Stack()
    is_balansed = True
    index = 0

    while index < len(bracket_string) and is_balansed:
        character = bracket_string[index]
        if character == '(':
            right_brackets.push(character)
        else:
            if right_brackets.size() == 0:
                is_balansed = False
            else:
                right_brackets.pop()
        index += 1

    if is_balansed and right_brackets.size() == 0:
        return True
    return False


def calculate(stack):
    stack_result = Stack()
    while stack.size() > 0:
        item = stack.pop()
        if isinstance(item, int):
            stack_result.push(item)
        else:
            if item == '+':
                stack_result.push(stack_result.pop() + stack_result.pop())
            elif item == '*':
                stack_result.push(stack_result.pop() * stack_result.pop())
            elif item == '-':
                stack_result.push(stack_result.pop() - stack_result.pop())
            elif item == '=':
                return stack_result.pop()
    return stack_result.pop()


def string_calculate(string_calc):
    calc_stack = Stack()
    for i in reversed(string_calc.split(" ")):
        try:
            calc_stack.push(int(i))
        except ValueError:
            calc_stack.push(i)

    return calculate(calc_stack)


def test_balansed():
    assert check_balansed("(()((())()))")
    assert not check_balansed("(()()(()")
    assert not check_balansed("(")
    assert not check_balansed(")")
    assert check_balansed("()")
    assert check_balansed("(()()()()(()(())))")


def test_calculate():
    assert string_calculate("1 2 + 3 * =") == 9
    assert string_calculate("8 2 + 5 * 9 + =") == 59
    assert string_calculate("2 2 - =") == 0


if __name__ == '__main__':
    test_balansed()
    test_calculate()