# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.add_two_simple_helper(l1, l2, 0)

    def add_two_simple_helper(self, l1, l2, carry):

        if not l1 and not l2:
            if carry:
                return ListNode(carry)
            else:
                return None

        n1 = 0
        n2 = 0

        nextl1 = None
        nextl2 = None
        if l1:
            n1 = l1.val
            nextl1 = l1.next

        if l2:
            n2 = l2.val
            nextl2 = l2.next

        sum = n1+n2+carry
        carry = int(sum/10)
        current = sum%10
        root = ListNode(current)
        root.next = self.add_two_simple_helper(nextl1, nextl2, carry)
        return root

if __name__ == '__main__':
     root1 = ListNode(2)
     root1.next = ListNode(4)
     root1.next.next = ListNode(3)

     root2 = ListNode(5)
     root2.next = ListNode(6)
     root2.next.next = ListNode(4)

     print(Solution().addTwoNumbers(root1, root2))