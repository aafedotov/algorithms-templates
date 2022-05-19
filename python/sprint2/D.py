# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
#

def solution(head, value) -> int:
    node = head
    index = 0
    while node:
        if node.value == value:
            return index
        node = node.next_item
        index += 1
    return -1


# node3 = Node("node3", None)
# node2 = Node("node2", node3)
# node1 = Node("node1", node2)
# node0 = Node("node0", node1)


# print(get_node_by_value(node0, 'node4'))