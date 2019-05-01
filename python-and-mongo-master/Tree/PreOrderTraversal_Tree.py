from Tree.Node import Node

def printInOrderTraversal(node):
    if node == None:
        return
    printInOrderTraversal(node.left)
    print(node.data)
    printInOrderTraversal(node.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    "Level order traversal of binary tree is -"
    printInOrderTraversal(root)


