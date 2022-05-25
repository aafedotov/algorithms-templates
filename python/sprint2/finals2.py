# ID 68595900

OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}


class Stack:
    """Класс, описывающий стек на списке."""
    def __init__(self):

        self.items = []

    def is_empty(self):

        return not self.items

    def push(self, value):

        self.items.append(value)

    def pop(self):

        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self.items.pop()


def calculator(values):
    """Задание B. Калькулятор для обратной польской нотации. """
    stack = Stack()
    for char in values:
        if char in OPERATORS:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            current_result = OPERATORS[char](operand_1, operand_2)
            stack.push(current_result)
        else:
            stack.push(int(char))
    return stack.pop()


def main():

    values = list(input().split())
    print(calculator(values))


if __name__ == '__main__':

    main()
