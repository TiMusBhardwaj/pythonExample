# find-maximum-sum-root-to-leaf-path-binary-tree

class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

#
# This method is based on the fact , all path except max_path
# will end in Null before decremented sum goes to Zero
def print_max_sum_tree_path(root, sum):

    if sum ==0:
        return True
    if root is None:
        return False
    left = print_max_sum_tree_path(root.left, sum - root.data)
    right = print_max_sum_tree_path(root.right, sum - root.data)

    if left or right:
        print(root.data, end="->")
    return left or right


#  max sum from left sub tree and max sum from right tree
# Compare left and right values and add the higher value to the root node
def max_sum_root_to_leaf(root):
    if not root:
        return

    max_sum_left = 0 if root.left is None else max_sum_root_to_leaf(root.left)
    max_sum_right = 0 if root.right is None else max_sum_root_to_leaf(root.right)

    return max_sum_left + root.data if max_sum_left > max_sum_right else max_sum_right + root.data

# Find max sum and print max sum Path
def find_max_sum_and_print(root):
    max_sum = max_sum_root_to_leaf(root)
    print("Max Sum from root to Leaf Node is :", max_sum)
    print("Path of max_sum : ")
    print_max_sum_tree_path(root, max_sum)

# Driver
if __name__ == '__main__':
    root = Node(1);
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(8)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(10)
    root.right.left.left = Node(7)
    root.right.left.right = Node(9)
    root.right.right.right = Node(5)

    find_max_sum_and_print(root)