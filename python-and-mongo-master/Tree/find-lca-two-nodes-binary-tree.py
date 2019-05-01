class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# This Methods finds Lca and also verify both node are present in tree
def find_lca_and_check_nodes_present(root, n1, n2):
    findLCA.n1 = False
    findLCA.n2 = False
    lca = findLCA(root, n1, n2)
    if findLCA.n1 and findLCA.n2:
        return lca
    else:
        return Node(None)


# This function returns pointer to LCA of two given
# values n1 and n2
# This function also verify that n1 and n2 are present in
# Binary Tree
def findLCA(root, n1, n2):
    if not root:
        return root

    # findLCA.n1 and findLCA.n2 are boolean variables to verify nodes exists in tree.
    #    Current node Match n1
    if root.data == n1:
        findLCA.n1 = True
    #   Current node Match n2
    if root.data == n2:
        findLCA.n2 = True

    # Both have been Matched no need to go any further.
    # This condition is added for scenario where both nodes are found no need to
    # further down the tree.
    if findLCA.n1 and findLCA.n2:
        return root

    # if lca_left not null atleast one of the nodes is present in left sub tree
    lca_left = findLCA(root.left, n1, n2)
    # Both have been Matched no need to go any further.
    # These condition is added for scenario where one of the node is LCA
    if findLCA.n1 and findLCA.n2:
        return lca_left
    # if lca_right not null at least one of the nodes is present in right sub tree
    lca_right = findLCA(root.right, n1, n2)

    # This condition is added for scenario where one of the requested node is LCA
    # Here we will override the child result received from parent node
    if root.data == n1 or root.data == n2:
        return root

    # if one node is present in left subtree and other in right subtree.
    # this will be your lowest common ancestor
    if lca_left and lca_right:
        return root

    # return if any of the subtree returned a result
    return lca_right if lca_right else lca_left


if __name__ == '__main__':
    root = Node(1)
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4,5) = ", find_lca_and_check_nodes_present(root, 4, 5).data)
    print("LCA(4,6) = ", find_lca_and_check_nodes_present(root, 4, 6).data)
    print("LCA(3,4) = ", find_lca_and_check_nodes_present(root, 3, 4).data)
    print("LCA(2,4) = ", find_lca_and_check_nodes_present(root, 2, 4).data)
    print("LCA(6,7) = ", find_lca_and_check_nodes_present(root, 6, 7).data)
    print("LCA(6,33) = ", find_lca_and_check_nodes_present(root, 6, 33).data)
    print("LCA(8,33) = ", find_lca_and_check_nodes_present(root, 8, 33).data)
