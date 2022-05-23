# ID 68552455

import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


class Stack:
    """Класс, описывающий стек на списке."""
    def __init__(self):

        self.items = []

    def push(self, value):

        self.items.append(value)

    def pop(self):

        return self.items.pop()


def calculator(values):
    """Задание B. Калькулятор для обратной польской нотации. """
    result = Stack()
    for char in values:
        if char in OPERATORS:
            operand_2 = result.pop()
            operand_1 = result.pop()
            current_result = OPERATORS[char](operand_1, operand_2)
            result.push(current_result)
        else:
            result.push(int(char))
    return result.pop()


def main():

    values = list(input().split())
    print(calculator(values))


if __name__ == '__main__':

    main()
