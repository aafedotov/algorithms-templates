# ID 68595173

class DeQueueSized:
    """Задание А. Класс, описывающий дек на кольцевом буфере."""

    def __init__(self, max_size):

        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def is_full(self):
        return self.max_size == self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def push_back(self, value):

        if self.is_full():
            raise IndexError
        self.queue[self.tail] = value
        self.queue_size += 1
        self.tail = (self.tail + 1) % self.max_size
        return None

    def push_front(self, value):

        if self.is_full():
            raise IndexError
        self.queue[self.head - 1] = value
        self.head = (self.head - 1) % self.max_size
        self.queue_size += 1
        return None

    def pop_front(self):

        if self.is_empty():
            raise IndexError
        result = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.queue_size -= 1
        return result

    def pop_back(self):

        if self.is_empty():
            raise IndexError
        result = self.queue[self.tail - 1]
        self.queue[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.queue_size -= 1
        return result


COMMANDS = {
    'push_front': DeQueueSized.push_front,
    'push_back': DeQueueSized.push_back,
    'pop_front': DeQueueSized.pop_front,
    'pop_back': DeQueueSized.pop_back
}


def main():

    n = int(input())
    size = int(input())
    dequeue = DeQueueSized(size)
    for i in range(0, n):
        current_command = list(input().split())
        try:
            if len(current_command) == 1:
                print(COMMANDS[current_command[0]](dequeue))
            elif len(current_command) == 2:
                COMMANDS[current_command[0]](dequeue, current_command[1])
            else:
                print('invalid command')
        except IndexError:
            print('error')


if __name__ == '__main__':

    main()
