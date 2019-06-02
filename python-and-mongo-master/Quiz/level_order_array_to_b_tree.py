# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def array_to_b_tree(self, arr) -> TreeNode:
        if len(arr) == 0:
            return None
        root = TreeNode(arr[0])
        node_arr = [root]
        index = 1
        while True:
            if index >= len(arr):
                break
            parent = node_arr.pop(0)
            while not parent.val:
                parent = node_arr.pop(0)
            left = TreeNode(arr[index])
            parent.left = left
            index +=1
            if index >= len(arr):
                break
            right = TreeNode(arr[index])
            parent.right = right
            index +=1
            node_arr.append(parent.left)
            node_arr.append(parent.right)

        return root

if __name__ == '__main__':
    Solution().array_to_b_tree([5,3,6,2,4,None,8,1,None,None,None,7,9, 6, 66, 67])