#
# class DoubleConnectedNode:
#     def __init__(self, value, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev
#
#     def __str__(self):
#         return self.value
#
#
# def print_all(node) -> None:
#     while node:
#         print(node.value)
#         node = node.next
#
#
# def test():
#     node3 = DoubleConnectedNode("node3")
#     node2 = DoubleConnectedNode("node2")
#     node1 = DoubleConnectedNode("node1")
#     node0 = DoubleConnectedNode("node0")
#     node0.next = node1
#     node1.prev = node0
#     node1.next = node2
#     node2.prev = node1
#     node2.next = node3
#     node3.prev = node2
#     new_head = solution(node0)
#     print_all(new_head)
#     # result is new_head == node3
#     # node3.next == node2
#     # node2.next == node1 node2.prev == node3
#     # node1.next == node0 node1.prev == node2
#     # node0.prev == node1


def solution(node):
    current_node = node

    while node:
        current_node = node
        node_next = node.next
        node.next = node.prev
        node.prev = node_next
        node = node.prev
    return current_node


# test()