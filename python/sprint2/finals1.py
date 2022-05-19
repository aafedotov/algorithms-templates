class DeQueueSized:
    """Класс, описывающий дек на кольцевом буфере."""

    def __init__(self, max_size):

        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push_back(self, value):

        if self.queue_size != self.max_size:
            self.queue[self.tail] = value
            self.queue_size += 1
            self.tail = (self.tail + 1) % self.max_size
            return None
        return 'error'

    def push_front(self, value):

        if self.queue_size != self.max_size:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_size
            self.queue_size += 1
            return None
        return 'error'

    def pop_front(self):

        if self.queue_size != 0:
            result = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.queue_size -= 1
            return result
        return 'error'

    def pop_back(self):

        if self.queue_size != 0:
            result = self.queue[self.tail - 1]
            self.queue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_size
            self.queue_size -= 1
            return result
        return 'error'


def main():

    n = int(input())
    size = int(input())
    dequeue = DeQueueSized(size)
    for i in range(0, n):
        current_command = list(input().split())
        if current_command[0] == 'push_front':
            result = dequeue.push_front(current_command[1])
            if result:
                print(result)
        if current_command[0] == 'push_back':
            result = dequeue.push_back(current_command[1])
            if result:
                print(result)
        if current_command[0] == 'pop_front':
            print(dequeue.pop_front())
        if current_command[0] == 'pop_back':
            print(dequeue.pop_back())


if __name__ == '__main__':

    main()
