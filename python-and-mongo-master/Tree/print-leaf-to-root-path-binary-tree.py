# https://www.techiedelight.com/print-leaf-to-root-path-binary-tree/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Chcek if leaf node
def is_leaf_node(node):
    if node and not node.left and not node.right:
        return True
    else:
        return False


# This Function uses iterative pre order traversal.
# Path is pushed down in the tree along with node.
# Path is Printed when a leaf node is encountered
def print_leaf_to_head_path(root):
    if root is None:
         return
    root.path = str(root.data)
    arr = [root]
    while arr.__len__() > 0:
        node = arr.pop()

        # Print Path if child node
        if is_leaf_node(node):
            print(node.path)

        # Pass  Path from top to current with to child node
        if node.left is not None:
            node.left.path = str(node.left.data) + "->" + node.path
            arr.append(node.left)

        if node.right is not None:
            node.right.path = str(node.right.data) + "->" + node.path
            arr.append(node.right)


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

    print_leaf_to_head_path(root)