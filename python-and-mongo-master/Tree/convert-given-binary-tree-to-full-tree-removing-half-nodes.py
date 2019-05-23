# https://www.techiedelight.com/convert-given-binary-tree-to-full-tree-removing-half-nodes/
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Find if node is leaf node. left and right child should be None
def is_leaf_node(node):
    return not node.left and not node.right


# Print Tree nodes using in-order Traversal
def print_inorder(root):

    if not root:
        return
    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)


def truncate(root):
    if not root:
        return None

    root.left = truncate(root.left)
    root.right = truncate(root.right)
    if (root.left and root.right) or is_leaf_node(root):
        return root
    root = root.left if root.left else root.right

    return root


def truncate_half_nodes_and_print_tree(root):
    root = truncate(root)
    print_inorder(root)

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
    truncate_half_nodes_and_print_tree(root)
