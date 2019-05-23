# https://www.techiedelight.com/distance-between-given-pairs-of-nodes-binary-tree/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def findLevel(root, node, level):
    if not root:
        return None
    if root.data == node:
        return level+1
    left = findLevel(root.left, node, level+1)
    right = findLevel(root.right, node, level+1)

    if not left and not right:
        return None
    elif left:
        return left
    else:
        return right
# Function to find lowest common ancestor of given nodes n1 and n2 where
#  both n2 and n2 are present in the binary tree.
def find_lca_node(root, n1, n2):
    if not root or n1 == root.data or root.data == n2:
        return root

    lca_left = find_lca_node(root.left , n1, n2)
    lca_right = find_lca_node(root.right, n1, n2)

    if lca_left and lca_right:
        return root
    return lca_right if lca_right else lca_left

# Function to find distnce between 2 nodes
def find_distance_btw_two_nodes(root, n1, n2):
    level_n1 = findLevel(root, n1,0)
    if not level_n1:
        print(n1, " does not exists in Tree")
        return
    level_n2 = findLevel(root, n2, 0)
    if not level_n2:
        print(n2, " does not exists in Tree")
        return 
    lca = find_lca_node(root, n1, n2)
    level_lca = findLevel(root, lca.data, 0)
    return level_n1 + level_n2 - 2*level_lca


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


    print(find_distance_btw_two_nodes(root, 3,9))
    print(find_distance_btw_two_nodes(root, 2, 4))
    print(find_distance_btw_two_nodes(root, 4, 8))

