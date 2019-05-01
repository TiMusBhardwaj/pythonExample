# A binary tree node
class Node:

    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# This function returns pointer to LCA of two given
# values n1 and n2
# This function assumes that n1 and n2 are present in
# Binary Tree
def findLCA(root, n1, n2):
    if not root or root.key == n1 or root.key == n2:
        return root

    lca_left = findLCA(root.left, n1, n2)
    lca_right = findLCA(root.right, n1, n2)

    if lca_left and lca_right:
        return root

    return lca_left if lca_left is not None else lca_right

# Driver program to test above function

# Let us create a binary tree given in the above example


if __name__ == '__main__':
    root = Node(1)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print ("LCA(4,5) = ", findLCA(root, 4, 5).key)
    print ("LCA(4,6) = ", findLCA(root, 4, 6).key)
    print ("LCA(3,4) = ", findLCA(root, 3, 4).key)
    print ("LCA(2,4) = ", findLCA(root, 2, 4).key)

