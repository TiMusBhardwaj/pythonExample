class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def peek(stack):
    if len(stack) > 0:
        return stack[-1]
    return None

def inorder_traversel_iterative(root):
    arr=[]
    curr = root
    while arr.__len__()>0 or curr is not None:
        if curr:
            arr.append(curr)
            curr = curr.left
        else:
            curr = arr.pop()
            print(curr.data, )
            curr = curr.right


def preorder_traversel(root):
    if not root:
        return
    print(root.data, )
    preorder_traversel(root.left)

    preorder_traversel(root.right)


def pre_traversel_iterative(root):
    if not root:
        return
    arr=[root]
    #curr = root
    while arr.__len__()>0:
        node = arr.pop()

        print(node.data)
        if node.right:
            arr.append(node.right)
        if node.left:
            arr.append(node.left)

def inorder_traversel(root):
    if not root:
        return
    inorder_traversel(root.left)
    print(root.data, )
    inorder_traversel(root.right)

def postorder_traversel(root):
    if not root:
        return
    postorder_traversel(root.left)
    postorder_traversel(root.right)
    print(root.data, )


def postorder_traversel_iterative_2_stack(root):
    if not root:
        return
    arr1 = [root]
    arr2 = []
    while arr1.__len__() > 0:
        node = arr1.pop()
        arr2.append(node)
        if node.left:
            arr1.append(node.left)
        if node.right:
            arr1.append(node.right)
    print(arr2)


def postorder_traversel_iterative_1_stack(root):
    if not root:
        return
    arr = []
    res = []
    while True:
        while root:
            if root.right:
                arr.append(root.right)
            arr.append(root)
            root = root.left

        root = arr.pop()
        if root.right and root.right == peek(arr):
            arr.pop()
            arr.append(root)
            root = root.right
        else:
            res.append(root.data)
            root = None
        if (len(arr) <= 0):
            break
    print(res)

def l_helper(arr, node):
    if node is None:
        if arr.__len__() == 0:
            pass
            #break;
        else:
            arr.append(None)
            #continue



def l_traversel(root):
    if root is None:
        return

    arr = [root, None]
    res = []
    reverse = True
    while arr.__len__() > 0:
        if arr[0] is None:
            if arr.__len__() == 1:
                break;
            else:
                arr.append(arr.pop(0))
                continue
        if reverse:
            index_none = arr.index(None)
            while index_none > 0:
                index_none -=1
                node = arr.pop(index_none)
                res.append(node.data)

                if node.right:
                    arr.append(node.right)
                if node.left:
                    arr.append(node.left)
        else:
            index_none = arr.index(None)
            counter =0
            while counter < index_none:
                counter+=1
                node = arr.pop(0)
                res.append(node.data)
                if node.right:
                    arr.append(node.right)
                if node.left:
                    arr.append(node.left)

        reverse = not reverse



    print(res)

"""
                      1
               2             3
        4          5            7
                 8     
               9 
            10 


"""
if __name__ == '__main__':
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

    postorder_traversel_iterative_2_stack(root)
    postorder_traversel(root)

