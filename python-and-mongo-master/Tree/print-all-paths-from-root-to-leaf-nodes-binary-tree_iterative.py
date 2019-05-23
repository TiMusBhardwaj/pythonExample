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
        print(str(arr[counter].data) , end=" -> ")
        counter = counter-1
    print(arr[0].data)

# Chcek if leaf node
def is_leaf_node(node):
    if node and not node.left and not node.right:
        return True
    else:
        return False

def peek(arr):
    if not arr and arr.__len__()==0:
        return None
    else:
        return arr[arr.__len__()-1]


# Recursive function to print all paths from leaf to root node
def print_leaf_to_root_paths_iterative(root):
    if not root:
        return

    arr = [root]
    print_array = []
    while arr.__len__() > 0:
        node = arr.pop()
        print_array.append(node)
        if is_leaf_node(node):
            print_arr(print_array)
            if arr.__len__() == 0:
                break
            # pop till you reach a branched parent.
            # This will starting point of another path
            while print_array.__len__()>0:
                print_node = print_array.pop()
                if print_node.right == peek(arr):
                    print_array.append(print_node)
                    break

        if node.right:
            arr.append(node.right)

        if node.left:
            arr.append(node.left)


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
    print_leaf_to_root_paths_iterative(root)
