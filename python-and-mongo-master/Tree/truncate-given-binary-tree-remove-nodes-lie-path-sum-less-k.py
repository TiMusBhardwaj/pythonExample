# https://www.techiedelight.com/truncate-given-binary-tree-remove-nodes-lie-path-sum-less-k/

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Print Tree nodes using pre-order Traversal
def print_pre_order(root):

    if not root:
        return
    print(root.data)
    print_pre_order(root.left)
    print_pre_order(root.right)

# if sum of nodes in path from root node to current node is more than or equal to K,
# nothing needs to be done and return True.
# If you have reached None that means total sum was less than given value return False
# if any of left or right subtree has path length less than the given value. Remove that path
def truncate(root, k, sum):
    if root is None:
        return False

    if sum + root.data >= k:
        return True

    left = truncate(root.left, k, sum + root.data)
    if not left:
        root.left = None
    right = truncate(root.right, k, sum + root.data)
    if not right:
        root.right = None
    return left or right


def truncate_and_print(root, k):
    truncate(root, k, 0)
    print_pre_order(root)


if __name__ == '__main__':
    root = Node(6)
    root.left = Node(3)
    root.right = Node(8)
    root.right.left = Node(4)
    root.right.right = Node(2)
    root.right.left.left = Node(1)
    root.right.left.right = Node(7)
    root.right.right.right = Node(3)

    truncate_and_print(root, 20)


