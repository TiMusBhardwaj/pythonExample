#https://www.techiedelight.com/spiral-order-traversal-binary-tree/
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


# Method to print tree in zig zag manner using iterative method
def spiral_order_traversal_iterative(root):
    if not root:
        return
    arr = [root]
    # varibale to switch printing order
    order = True
    while arr.__len__()>0:
        length = arr.__len__()
        while length>0:
            length = length -1
            # Print from starting of array
            if order:
                node = arr.pop(0)
                print(node.data)
                if node.left:
                    arr.append(node.left)
                if node.right:
                    arr.append(node.right)
            # # Print from Back of the array
            else:
                node = arr.pop()
                print(node.data)
                if node.right:
                    arr.insert(0, node.right)
                if node.left:
                    arr.insert(0, node.left)
        # Change the printing order
        order = not order


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
    spiral_order_traversal_iterative(root)
