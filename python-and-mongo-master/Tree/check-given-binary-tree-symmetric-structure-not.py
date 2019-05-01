
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

#Check left and right subtree for symmetry
def is_symmetric(node_a, node_b):
    if not node_a and not node_b:
        return True

# return true if
# 1. both trees are non-empty and
# 2. left subtree is mirror image of right subtree and
# 3. right subtree is mirror image of left subtree
    return (node_a and node_b) and is_symmetric(node_a.left, node_b.right) and is_symmetric(node_a.right, node_b.left)

def is_sysmmetric(root):
    if not root:
        return True

    return is_symmetric(root.left, root.right)

#Driver program to check symmetry
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right= Node(5)

    if is_sysmmetric(root):
        print("Tree is Symmetric")
    else:
        print("Tree is not Symmetric")

    root.right.right.left= Node(6)
    if is_sysmmetric(root):
        print("Tree is Symmetric")
    else:
        print("Tree is not Symmetric")
