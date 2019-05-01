

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.data)
'''
This implementation uses level order traversal.
The vertical column right to root node are positive and to left of root node
is negative.
Dictionary(res) is used to keep track of lowest node in a vertical column.'''
def print_bottom_view_BT(root):
    if not root:
        return
    res = {}
    root.level = 0
    arr = [root]
    while arr.__len__() > 0:
        node = arr.pop(0)
        res[node.level] = node.data
        if node.left:
            node.left.level = node.level -1
            arr.append(node.left)
        if node.right:
            node.right.level = node.level + 1
            arr.append(node.right)
    print(sorted(res.items()))


#Driver Program
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    print_bottom_view_BT(root)
