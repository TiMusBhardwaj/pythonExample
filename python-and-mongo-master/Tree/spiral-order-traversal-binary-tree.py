#https://www.techiedelight.com/spiral-order-traversal-binary-tree/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Function to print level order traversal of given binary tree
def print_spiral_order(root):
    if not root:
        return
    level = 0
    while print_level_left_to_right(root, level = level+1) and print_level_right_to_left(root, level = level+2):
        level = level + 2



# Function to print all nodes of a given level from left to right
def print_level_left_to_right(root, level):
    if not root:
        return False

    if level ==1:
        print(root.data)
        return True
    left = print_level_left_to_right(root.left, level=level - 1)
    right = print_level_left_to_right(root.right, level=level - 1)
    return left or right


# Function to print all nodes of a given level from right to left
def print_level_right_to_left(root, level):
    if not root:
        return False

    if level ==1:
        print(root.data)
        return True
    right = print_level_right_to_left(root.right, level= level-1)
    left = print_level_right_to_left(root.left, level= level-1)
    return left or right


#Driver Program
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
    print_spiral_order(root)
