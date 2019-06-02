# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:

    def __init__(self):
        self.curr_node = TreeNode(None)

    def increasingBST(self, root: TreeNode) -> TreeNode:


        if root is None or (root.left is None and root.right is None):
            return root
        if root.right is not None:
            right = self.increasingBST(root.right)
            root.right = right
        if root.left is not None:
            left = self.increasingBST(root.left)
            t_left = left
            while t_left.right is not None:
                t_left = t_left.right

            t_left.right = root
            root.left = None
            root = left

        return root

    def increasingBST_better(self, root: TreeNode):

            if root is None :
                return
            if root.right is not None:
                self.increasingBST_better(root.right)
            root.right = self.curr_node
            self.curr_node = root
            if root.left is not None:
                self.increasingBST_better(root.left)
                root.left = None

            return


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
            while not parent:
                parent = node_arr.pop(0)
            left =  TreeNode(arr[index]) if arr[index] is not None else None
            parent.left = left
            index +=1
            if index >= len(arr):
                break
            right = TreeNode(arr[index]) if arr[index] is not None else None
            parent.right = right
            index +=1
            node_arr.append(parent.left)
            node_arr.append(parent.right)

        return root


if __name__ == '__main__':
    sol = Solution()

    root = sol.array_to_b_tree([5,3,6,2,4,None,8,1,None,None,None,7,9])
    sol.increasingBST_better(root)
    print(sol.curr_node)
