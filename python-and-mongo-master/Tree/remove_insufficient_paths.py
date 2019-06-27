# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        leftnode = self.sufficient_helper(root.left, limit, root.val)
        if not leftnode:
            root.left = None
        rightnode = self.sufficient_helper(root.right, limit, root.val)
        if not rightnode:
            root.right = None
        if leftnode or rightnode:
            return root
        else:
            return None

    def sufficient_helper(self, root: TreeNode, limit: int , sum):

        if not root:
            return True if sum >= limit else False

        leftnode = self.sufficient_helper(root.left, limit, sum+root.val)
        if not leftnode:
            root.left = None
        rightnode = self.sufficient_helper(root.right, limit, sum+root.val)
        if not rightnode:
            root.right = None
        return leftnode or rightnode

