# https://www.techiedelight.com/determine-given-binary-tree-is-a-bst-or-not/
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

INT_MAX = 4294967296
INT_MIN = -4294967296

# Print Tree nodes using in-order Traversal
def print_inorder(root):

    if not root:
        return
    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)


def is_bst(root, min, max):

    if root is None:
        return True

    if root.data < min or root.data > max:
        return False
    left = is_bst(root.left, min, root.data)
    if not left:
        return False
    right = is_bst(root.right, root.data, max)

    return left and right


def find_is_bst_and_print(root):
    bst = is_bst(root, INT_MIN, INT_MAX)
    print("Tree is BST : ", bst)

if __name__ == '__main__':
    root = Node(9)
    root.left = Node(2)
    root.right = Node(11)
    root.right.left = Node(1)
    root.right.right = Node(14)
    find_is_bst_and_print(root)
    root.right.left = Node(10)
    find_is_bst_and_print(root)