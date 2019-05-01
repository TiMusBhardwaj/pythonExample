from builtins import print

#Breath First Traversal for a tree

class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def minDepth(root):
    a = list()
    if(root == None):
        return 0
    #a.append(root)
    a.append({'node': root, 'depth': 1})
    while a.__len__() > 0 :
        item = a.pop(0)
        node = item['node']
        depth = item['depth']

        #print(node.data)
        #print("\n")
        # If this is the first leaf node seen so far
        # then return its depth as answer
        if node.left is None and node.right is None:
            return depth

        # If left subtree is not None, add it to queue
        if node.left is not None:
            a.append({'node': node.left, 'depth': depth + 1})

            # if right subtree is not None, add it to queue
        if node.right is not None:
            a.append({'node': node.right, 'depth': depth + 1})



        # Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)
root.right.right.right = Node(8)


"Level order traversal of binary tree is -"
print(minDepth(root))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(minDepth(root))