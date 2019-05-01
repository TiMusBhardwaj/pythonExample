
# TODO : Incomplete

class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

#This Functions used post order traversal

def is_sum_tree(root):
    if not root:
        return True,0

    is_sum_tree_left, sum_left = is_sum_tree(root.left)
    if not is_sum_tree_left:
        return False

    is_sum_tree_right, sum_right = is_sum_tree(root.right)
    if not is_sum_tree_right:
        return False

    return