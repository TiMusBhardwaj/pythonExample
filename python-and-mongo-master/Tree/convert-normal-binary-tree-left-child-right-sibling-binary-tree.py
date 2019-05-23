# https://www.techiedelight.com/convert-normal-binary-tree-left-child-right-sibling-binary-tree/

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Print Tree nodes using in-order Traversal
def print_inorder(root):

    if not root:
        return
    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)

#  Function to convert a normal binary tree to Left-child
#  right-sibling (LC-RS) binary tree
def convert(root):
    if root is None:
        return

    left = convert(root.left)
    right = convert(root.right)
    # If its left child is empty, then make its right child as left and set right to null
    if left is None and right:
        root.left = right
    # If left child already exists,
    # then make right child of its left child to point to its right child and set right child to null.
    elif left and right:
        root.left= left
        root.left.right = right
        root.right = None
    return root

def convert_and_print(root):
    convert(root)
    print_inorder(root)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    convert_and_print(root)