# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def __repr__(self):
         return str(self.val)



class Solution:
    def mergeKLists(self, lists) -> ListNode:

        length = len(lists)
        last = length - 1
        while last > 0:
            start = 0

            while start < last:
                lists[start] = self.mergeTwoLists_iterative(lists[start], lists[last])
                start += 1
                last -= 1

        return lists[0]

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
            curr.next = l1
        else:
            curr.next = l2

        return temp_head.next

if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    node.next.next.next.next.next = ListNode(6)

    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    node1.next.next.next.next.next = ListNode(6)


    node2 = ListNode(1)
    node2.next = ListNode(2)
    node2.next.next = ListNode(3)
    node2.next.next.next = ListNode(4)
    node2.next.next.next.next = ListNode(5)
    node2.next.next.next.next.next = ListNode(6)

    Solution().mergeKLists([node, node1, node2])