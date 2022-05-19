class MyQueueSized:

    def __init__(self, max_size):

        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push(self, value):

        if self.queue_size != self.max_size:
            self.queue[self.tail] = value
            self.queue_size += 1
            self.tail = (self.tail + 1) % self.max_size
            return None
        print('error')
        return None

    def pop(self):

        if self.queue_size != 0:
            print(self.queue[self.head])
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.queue_size -= 1
            return None
        print('None')
        return None

    def peek(self):

        if self.queue_size != 0:
            print(self.queue[self.head])
            return None
        print('None')
        return None

    def size(self):
        return self.queue_size


def main():

    n = int(input())
    size = int(input())
    queue = MyQueueSized(size)
    for i in range(0, n):
        current_command = list(input().split())
        if current_command[0] == 'pop':
            queue.pop()
        if current_command[0] == 'push':
            queue.push(int(current_command[1]))
        if current_command[0] == 'peek':
            queue.peek()
        if current_command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':

    main()


