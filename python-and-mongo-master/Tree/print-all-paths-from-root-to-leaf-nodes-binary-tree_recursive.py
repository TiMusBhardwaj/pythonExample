#https://www.techiedelight.com/print-all-paths-from-root-to-leaf-nodes-binary-tree/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def print_arr(arr):
    if not arr or arr.__len__() == 0:
        return
    counter = arr.__len__() -1
    while counter >= 1:
        print(str(arr[counter]) , end=" -> ")
        counter = counter-1
    print(arr[0])

# Chcek if leaf node
def is_leaf_node(node):
    if node and not node.left and not node.right:
        return True
    else:
        return False


# Recursive function to print all paths from leaf to root node
def print_leaf_to_root_paths(root , arr):
    if not root:
        return
    arr.append(root)
    if is_leaf_node(root):
        print_arr(arr)
    if root.left:
        print_leaf_to_root_paths(root.left, arr)
    if root.right:
        print_leaf_to_root_paths(root.right, arr)
    # Pop Current node as this is a common array and this path is complete now.
    # After pop this array will be reused up in the tree
    arr.pop()

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
    print_leaf_to_root_paths(root, [ ])
