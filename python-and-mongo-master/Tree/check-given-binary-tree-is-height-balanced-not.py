# https://www.techiedelight.com/check-given-binary-tree-is-height-balanced-not/
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Recursive function to check if given binary tree is height balanced or not
def is_height_balanced(root):
    # Reached leaf Node
    if root is None:
        return 0, True

    # Check if left tree is balanced, also get its height
    h_left, is_balanced_l = is_height_balanced(root.left)
    # If un-balanced no further action required
    if not is_balanced_l:
        return 0, False
    # Check if right is balanced also get its height
    h_right, is_balanced_r = is_height_balanced(root.right)
    # If un-balanced no further action required
    if not is_balanced_r:
        return 0, False

    # Check if current node is unbalanced
    if abs(h_right - h_left) > 1:
        return 0, False
    # If everything is balanced till now, return height up in Tree
    return max(h_left, h_right) + 1, True

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print("Tree is Balanced :", is_height_balanced(root).__getitem__(1))

    root.right.left.right = Node(7)
    print("Tree is Balanced :", is_height_balanced(root).__getitem__(1))


