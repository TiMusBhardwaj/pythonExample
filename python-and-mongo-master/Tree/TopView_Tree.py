from builtins import print

#Breath First Traversal for a tree

class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printTopView(root):
    a = list()
    level_dict = dict()
    if(root == None):
        return
    root.level=0
    a.append(root)
    while a.__len__() > 0 :
        tempNode = a.pop(0)
        level = tempNode.level
        h_node = level_dict.get(level)
        if not h_node:
            print(tempNode.data)
            level_dict[level] = tempNode

        #print(tempNode.data)
        #print("\n")
        if(tempNode.left != None):
            tempNode.left.level = level -1
            a.append(tempNode.left)
        if(tempNode.right != None):
            tempNode.right.level = level + 1
            a.append(tempNode.right)



# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.left.right.left.left = Node(9)
root.left.right.left.left.left = Node(10)
root.right.right = Node(7)


"Level order traversal of binary tree is -"
printTopView(root)