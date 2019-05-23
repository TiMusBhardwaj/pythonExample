# https://www.techiedelight.com/sink-nodes-containing-zero-bottom-binary-tree/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Print Tree data using pre order traversal
def preorder_traversal(root):
    if not root:
        return
    print(root.data, )
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# Swap data of a node containing 0 with one of its child
# Repeat recursively till leaf node is encountered or a node with 0 is encountered
def sink(root):
    if not root:
        return

    if root.left and root.left.data != 0:
        root.data, root.left.data = root.left.data, root.data
        sink(root.left)
    elif root.right and root.right.data != 0:
        root.data, root.right.data = root.right.data, root.data
        sink(root.right)

# This Method uses post order traversal to sink 0 in left and right subtree and then moving to root
# Where a 0 is encountered it is sinked using @sink(root)
def sinkNode(root):
    if not root:
        return
    sinkNode(root.left)
    sinkNode(root.right)
    if root.data == 0:
        sink(root)

# Sink 0 and print updated tree
def sink_tree_and_print(root):
    sinkNode(root)
    preorder_traversal(root)

# Driver
if __name__ == '__main__':

    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(2)
    root.right.left.left = Node(3)
    root.right.left.right = Node(4)
    sink_tree_and_print(root)