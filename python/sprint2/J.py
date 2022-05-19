class Node:

    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item


class NodeQueue:

    def __init__(self):
        self.queue_size = 0
        self.head = None
        self.tail = None

    def get(self):

        if self.queue_size != 0:
            print(self.head.value)
            self.head = self.head.next_item
            self.queue_size -= 1
            return None
        print('error')
        return None

    def put(self, value):

        if not self.head:
            self.head = Node(value=value)
            self.queue_size += 1
            return None
        new_node = Node(value=value)
        node = self.head
        while node.next_item:
            node = node.next_item
        node.next_item = new_node
        self.queue_size += 1

    def size(self):
        return self.queue_size


def main():

    n = int(input())
    queue = NodeQueue()
    for i in range(0, n):
        current_command = list(input().split())
        if current_command[0] == 'get':
            queue.get()
        if current_command[0] == 'put':
            queue.put(int(current_command[1]))
        if current_command[0] == 'size':
            print(queue.size())


if __name__ == '__main__':

    main()