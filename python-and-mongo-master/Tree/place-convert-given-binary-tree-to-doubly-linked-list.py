
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

class List_Node:

    # Constructor to create a node node in linked list
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)


# Print doubly linked List
def print_dll(head):
    if not head:
        return

    while head.next:
        print(head.data, end="<->")
        head = head.next
    print(head.data)

# This Method converts Tree into Doubly Linked List using reverse in order traversal
def convert(root, head):
    if not root:
        return None

    # recursively convert right subtree
    if root.right:
        head = convert(root.right, head)

    node = List_Node(root.data)
    # Move head to newly created node, previous head will become next
    if head:
        node.next, head.prev = head, node
    head = node

    #recursivly convert left subtree
    if root.left:
        head = convert(root.left, head)
    return head

# This Method converts Tree into Doubly Linked List using reverse in order traversal
def convert_and_print(root):
    head = None
    head = convert(root, head)
    print_dll(head)


# Driver Program
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(8)
    root.left.right.left.left = Node(9)
    root.left.right.left.left.left = Node(10)
    root.right.right = Node(7)
    convert_and_print(root)