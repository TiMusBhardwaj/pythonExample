# https://www.techiedelight.com/print-diagonal-traversal-binary-tree/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Function to print diagonal traversal of tree
def print_diagonal_traversal(root):
    if not root:
        return
    diagonal_array = [root]
    while root.right:
        diagonal_array.append(root.right)
        root = root.right
    # Diagonals in this array is separated by None
    diagonal_array.append(None)

    while diagonal_array.__len__()>0:
        node = diagonal_array.pop(0)
        # None indicates your diagonal is complete
        # Start with new diagonal if it exists
        if node is None and diagonal_array.__len__() ==0:
            break
        elif node is None:

            diagonal_array.append(None)
            # Just to give a line break for next diagonal
            print("")
            continue
        print(node.data, end=" ")
        # Move to next diagonal
        node = node.left
        # All elements right to node here
        while node:
            # All node right to given node will be part of same diagonal
            diagonal_array.append(node)
            node = node.right



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

    print_diagonal_traversal(root)



