
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def __repr__(self):
         return str(self.val)

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = head
        if node is None:
            return node
        length = 1
        while node.next is not None:
            length +=1
            node = node.next

        node.next = head
        if k > length:
            k = k%length
        break_node = length - k

        while break_node >0:
            node = node.next
            break_node -=1
        head = node.next
        node.next = None
        return head



if __name__ == '__main__':

    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)

    Solution().rotateRight(node,2)
