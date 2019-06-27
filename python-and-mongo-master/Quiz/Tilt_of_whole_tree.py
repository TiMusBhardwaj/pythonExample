# Definition for a binary tree node.
class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root):
        self.tilt =0
        self.findTilt_helper(root)
        return self.tilt
    def findTilt_helper(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        l_sum = self.findTilt_helper(root.left)
        r_sum = self.findTilt_helper(root.right)
        self.tilt += abs(l_sum - r_sum)
        return l_sum +r_sum + root.val


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    Solution().findTilt(root)