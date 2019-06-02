# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        node = head
        length = 0
        while node is not None :
            node = node.next
            length +=1

        root = self.sortedListToBST_helper(head, length)
        return root

    def sortedListToBST_helper(self, head, n):

        if n == 0:
            return None
        if n ==1:
            return TreeNode(head.val)

        mid = int(n/2)+1
        node = head
        count = 1
        while count < mid:
            node = node.next
            count +=1

        root = TreeNode(node.val)
        root.left = self.sortedListToBST_helper(head, mid -1)
        root.right = self.sortedListToBST_helper(node.next, n-mid)
        return root



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    Solution().sortedListToBST(head)
