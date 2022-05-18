class StackMaxEffective:

    def __init__(self):

        self.items = []
        self.maximums = []

    def push(self, value):

        if not self.maximums:
            self.maximums.append(value)
        else:
            if value >= self.maximums[-1]:
                self.maximums.append(value)
        self.items.append(value)

    def pop(self):

        if self.items:
            to_pop = self.items.pop()
            if to_pop == self.maximums[-1]:
                self.maximums.pop()
            return None
        print('error')
        return None

    def get_max(self):

        if self.items:
            return self.maximums[-1]
        return None


def main():

    n = int(input())
    stack = StackMaxEffective()
    for i in range(0, n):
        current_command = list(input().split())
        if current_command[0] == 'pop':
            stack.pop()
        if current_command[0] == 'push':
            stack.push(int(current_command[1]))
        if current_command[0] == 'get_max':
            print(stack.get_max())


main()


