
#https://www.techiedelight.com/check-if-two-binary-trees-are-identical-not-iterative-recursive/
# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Recursive function to check if two given binary trees are  identical or not
def is_identical_recursive(root1, root2):
    # If both tree is null return true
    if not root1 and not root2:
        return True
    # if both trees are non-empty and value of their root node matches,
    #  recurse for their left and right sub-tree
    if (root1 and root2) and (root1.data == root2.data) :
        return is_identical_recursive(root1.left, root2.left) and is_identical_recursive(root1.right , root2.right)
    else:
        return False


def is_node_equal(node1, node2):
    return node1 and node2 and node1.data == node2.data


def is_identical_iterative(root1, root2):
    # If both tree is null return true
    if not root1 and not root2:
        return True
    # If only one of them is null
    elif (root1 and not root2) or (not root1 and root2):
        return False

    # create a stack to hold Node pairs
    arr = [[root1,root2]]

    # do till stack is not empty
    while arr.__len__()>0:
        #  pop top pair from the stack and process it
        node_array = arr.pop(0)
        node1 = node_array.pop()
        node2 = node_array.pop()
        # if value of their root node don't match, return false
        if not is_node_equal(node1, node2):
            return False
        # Push left node pair if that exists
        if node1.left and node2.left:
            arr.append([node1.left, node2.left])
        # If only one of them exists
        elif node1.left or node2.left:
            return False
        # Push right node pair if that exists
        if node1.right and node2.right:
            arr.append([node1.right, node2.right])
        # If only one of them exists
        elif node1.right or node2.right:
            return False
    #if we reach here, both binary trees are identical
    return True




    # if both trees are non-empty and value of their root node matches,
    #  recurse for their left and right sub-tree
    if (root1 and root2) and (root1.data == root2.data):
        return is_identical_recursive(root1.left, root2.left) and is_identical_recursive(root1.right , root2.right)
    else:
        return False



# Driver Program
if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.left.right.left = Node(8)
    root1.left.right.left.left = Node(9)
    root1.left.right.left.left.left = Node(10)
    root1.right.right = Node(7)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    root2.left.right.left = Node(8)
    root2.left.right.left.left = Node(9)
    root2.left.right.left.left.left = Node(10)
    root2.right.right = Node(7)
    print("root1 and root2 are Identical " if is_identical_iterative(root1, root2)
          else "root1 and root2 are not Identical ")
    root1.right.right.right = Node(11)
    print("root1 and root2 are Identical " if is_identical_iterative(root1, root2)
          else "root1 and root2 are not Identical ")
    root2.right.right.right = Node(11)
    print("root1 and root2 are Identical " if is_identical_recursive(root1, root2)
          else "root1 and root2 are not Identical ")
    root1.right.right.right = Node(12)
    print("root1 and root2 are Identical " if is_identical_recursive(root1, root2)
          else "root1 and root2 are not Identical ")



