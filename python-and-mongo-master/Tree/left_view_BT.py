# Python program to print left view of Binary Tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ExtendedNode:
    def __init__(self, node, level):
        self.data = node.data
        self.left = node.left
        self.right = node.right
        self.level = level


def leftView(root):
    mem = {}
    root.level = 0;
    arr = [ExtendedNode(root, 0)]
    for ele in arr:
        if mem.get(ele.level) is None:
            print(ele.data)
            mem[ele.level]=""
        if ele.left:
            arr.append(ExtendedNode(ele.left, ele.level +1))
        if ele.right:
            arr.append(ExtendedNode(ele.right, ele.level +1))

def leftView_2(root):

    arr = [ExtendedNode(root, 0)]
    current_level = 0
    for ele in arr:
        if current_level == ele.level:
            print(ele.data)
            current_level +=1
        if ele.left:
            arr.append(ExtendedNode(ele.left, ele.level +1))
        if ele.right:
            arr.append(ExtendedNode(ele.right, ele.level +1))





if __name__ == '__main__':
    # Driver program to test above function
    root = Node(12)
    root.left = Node(10)
    root.right = Node(20)
    root.right.left = Node(25)
    root.right.right = Node(40)
    root.right.right.right = Node(14)
    root.right.right.right.right = Node(15)
    root.right.right.right.right.right = Node(16)


    leftView(root)
    print("-"*20)
    leftView_2(root)