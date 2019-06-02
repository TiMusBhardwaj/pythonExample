class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def __repr__(self):
         return str(self.val)

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        node = head
        if node is None:
            return None
        even = ListNode(-1)
        even_r = even
        while node.next is not None:
            even_r.next = node.next
            even_r = even_r.next
            if node.next.next is None:
                break
            node.next = node.next.next
            node = node.next
            even_r.next = None

        node.next = even.next
        return head

if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    node.next.next.next.next.next = ListNode(6)
    Solution().oddEvenList(node)




