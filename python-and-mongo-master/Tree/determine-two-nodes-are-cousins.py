class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


#Here Level order traversel is used,
#None in arr is used to mark end of each level.
#We will add left and right node as pair to array
def isNodesCousin(root, n1, n2):
    n1Matched = False
    n2Matched = False

    if not root:
        return False
    arr=[[root], None]
    while arr.__len__()>0:
        #pop out sub array of left and right
        node_arr = arr.pop(0)
        if not node_arr and arr.__len__() == 0:
            return False
        elif not node_arr and arr.__len__() > 0:
            if n1Matched or n2Matched:
                return False
            arr.append(None)
            continue
        n1MatchedLocal = False
        n2MatchedLocal = False

        #Find if n1, n2 match with left and right present in sub array
        #If n1, n2, Both Found in same subarray return False
        #n1MatchLocal and n2matchLocal is updated if either n1 or n2 is Matched
        while node_arr.__len__()>0:
            node = node_arr.pop(0)
            if not node:
                continue
            if node.data == n1:
                n1MatchedLocal = True
            elif node.data == n2:
                n2MatchedLocal = True
            temp_array = []

            #Add left, right to the temp_arr
            #Add node_arr to arr
            if node.left:
                temp_array.append(node.left)
            if node.right:
                temp_array.append(node.right)
            if temp_array.__len__()>0:
                  arr.append(temp_array)

        #n1 and n2 have same parent
        if n1MatchedLocal and n2MatchedLocal:
            return False
        #One of the n1 and n2 Matched
        elif n1MatchedLocal:
            n1Matched = n1MatchedLocal
        elif n2MatchedLocal:
            n2Matched = n2MatchedLocal

        # n1 and n2 Matched having different parent
        if n1Matched and n2Matched:
            return True


    return False


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


    if isNodesCousin(root, 7,7):
        print("Cousins")
    else:
        print("Not Cousins")

    arr_in = [[4,5], [5,7], [7,7], [7,88]]
    for arr in arr_in:
        if isNodesCousin(root, arr[0],arr[1]):
            print("Cousins")
        else:
            print("Not Cousins")