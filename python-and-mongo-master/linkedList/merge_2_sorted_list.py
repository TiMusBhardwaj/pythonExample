# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        node =  None
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            node = l2
        else :
            l1.next = self.mergeTwoLists(l1.next, l2)
            node = l1
        return node

    def mergeTwoLists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp_head = ListNode(None)
        curr = temp_head
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        if l1:
            curr.next =l1
        else:
            curr.next = l2

        return temp_head.next

if __name__ == '__main__':
    node = ListNode(2)
    node2  = ListNode(1)
    Solution().mergeTwoLists(node2, None)