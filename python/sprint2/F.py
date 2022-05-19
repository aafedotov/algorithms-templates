class StackMax:

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.items:
            result = self.items.pop()
            return result
        print('error')
        return 'error'

    def get_max(self):
        if self.items:
            return max(self.items)
        return None


def main():

    n = int(input())
    stack = StackMax()
    for i in range(0, n):
        current_command = list(input().split())
        if current_command[0] == 'get_max':
            print(stack.get_max())
        if current_command[0] == 'pop':
            stack.pop()
        if current_command[0] == 'push':
            stack.push(int(current_command[1]))


main()

