class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None




#Recursive function to in-place convert the given binary tree to its
#sum tree by traversing the tree in postorder manner
def convert_to_sum_tree_recursive(root):
    if not root:
        return 0
    #recursively convert left and right subtree first before
	# processing the root node
    left = convert_to_sum_tree_recursive(root.left)
    right = convert_to_sum_tree_recursive(root.right)

    #Save Old value
    old = root.data

    #update root node value with sum of left and right tree
    root.data = left+right

    #return the updated value plus old value. It is equal to
	# sum of all elements present in sub-tree rooted at root node
    return old + root.data


#Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.left.right.left.left = Node(9)
root.left.right.left.left.left = Node(10)
root.right.right = Node(7)


"Tree sum of binary tree is -"
print(convert_to_sum_tree_recursive(root))