class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def get_max_diameter_BT(root):
    get_diameter.diameter =0
    get_diameter(root)
    return get_diameter.diameter

def get_diameter(root):

    if not root:
        return  0
    left_subtree_height = get_diameter(root.left)
    right_subtree_height = get_diameter(root.right)
    #diameter at current node
    c_diameter = left_subtree_height + right_subtree_height + 1

    #If diamtere at current node is more than max_diameter, set current diameter to max diameter.
    get_diameter.diameter = c_diameter if c_diameter > get_diameter.diameter else  get_diameter.diameter
    #return max height to up in tree
    return max(right_subtree_height, left_subtree_height) + 1


if __name__ == '__main__':
    # Driver program to test above function
    #TREE 1
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print(get_max_diameter_BT(root))

    #TREE 2
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    root.right.right = Node(4)
    root.right.right.right = Node(7)
    root.right.left.left = Node(5)
    root.right.left.right = Node(6)
    print(get_max_diameter_BT(root))

