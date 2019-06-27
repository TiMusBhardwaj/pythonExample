# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        arr1 = [root.left]
        arr2 = [root.right]

        while len(arr1)>0 and len(arr2)>0:

            node1 = arr1.pop()
            node2 = arr2.pop()
            if not node1 and not node2:
                continue
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    arr1.append(node1.left)
                    arr1.append(node1.right)
                    arr2.append(node2.right)
                    arr2.append(node2.left)
            else:
                return False

        if len(arr1) == 0 and len(arr2) ==0:
            return True
        return False