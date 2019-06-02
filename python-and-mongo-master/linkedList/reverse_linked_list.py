# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


def reverse_linked_list(node):


    if node is None or node.next is None:
        return node,node

    head, prev = reverse_linked_list(node.next)
    node.next = None
    prev.next = node
    return head, node


def reverse_list_and_print(node):
    head, node = reverse_linked_list(node)
    while(head.next):
        print(head.data , end ="->")
        head = head.next
    print(head.data)

if __name__ == '__main__':
    node = Node(1)


    reverse_list_and_print(node)



