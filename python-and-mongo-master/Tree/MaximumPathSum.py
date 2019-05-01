
# A Binary Tree Node
class Node:

    # Contructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findMaxUtil(root):
    # Base Case
    if root is None:
        return 0

    l = findMaxUtil(root.left)
    r = findMaxUtil(root.right)

    semiMax = max(max(l, r) + root.data, root.data)

    currMax = max(semiMax, l+r+ root.data)
    findMaxUtil.res = max(findMaxUtil.res, currMax)
    return semiMax
def findMaxSum(root):
    # Initialize result
    findMaxUtil.res = float("-inf")

    # Compute and return result
    findMaxUtil(root)
    return findMaxUtil.res


# Driver program
root = Node(10)
root.left = Node(2)
root.right = Node(10);
root.left.left = Node(2000);
root.left.right = Node(1000);
root.right.right = Node(-25);
root.right.right.left = Node(3);
root.right.right.right = Node(4);
print("Max path sum is ", findMaxSum(root))