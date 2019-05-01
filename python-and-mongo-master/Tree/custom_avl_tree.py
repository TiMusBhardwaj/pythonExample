

# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return str(self.val)

class AVL_Tree:


    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right, key)

        #update height of a tree
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases

        #case 1 left and left
        if balance > 1 and root.left.val > key:
            return self.rightRotate(root)

        if balance < -1 and root.right.val < key:
            return self.leftRotate(root)

        if balance > 1 and root.left.val <key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and root.right.val > key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root);

        return root;

    def rightRotate(self, a):

        middle = a.left
        extra_branch = middle.right

        #rotation
        middle.right = a
        a.left = extra_branch


       # Update heights
        a.height = 1 + max(self.getHeight(a.left),
                           self.getHeight(a.right))
        middle.height = 1 + max(self.getHeight(middle.left),
                           self.getHeight(middle.right))

        # Return the new root
        return middle


    def leftRotate(self, node):
        middle = node.right
        extra_branch = middle.left

        #Rotate
        middle.left = node
        node.right = extra_branch


        #update height
        middle.height = 1+ max(self.getHeight(middle.left), self.getHeight(middle.right))
        node.height = 1+ max(self.getHeight(node.left), self.getHeight(node.right))

        return middle


    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)










myTree = AVL_Tree()
root = None

root = myTree.insert(root, 10)
root = myTree.insert(root, 20)
root = myTree.insert(root, 30)
root = myTree.insert(root, 40)
root = myTree.insert(root, 50)
root = myTree.insert(root, 25)

"""The constructed AVL Tree would be 
			30 
		/ \ 
		20 40 
		/ \	 \ 
	10 25 50"""

# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.preOrder(root)
print()


