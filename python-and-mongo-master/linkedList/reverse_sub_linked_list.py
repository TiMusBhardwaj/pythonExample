#https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        node = head
        count =1
        start = None
        end = None
        last_temp = None
        while node is not None:
            if count == m-1:
                start = node
            if count == m :
                last = node
                last_temp = last
            if n > count > m :
                temp = node
                node = node.next
                temp.next = last_temp
                last_temp = temp
                count+=1
                continue
            if count == n:
                temp = node
                node = node.next
                temp.next = last_temp
                last_temp = temp
                last.next = node
                if start is not None:
                    start.next = last_temp
                    return head
                else :
                    start = last_temp
                    return start
            node = node.next
            count +=1


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    node.next.next.next.next.next = ListNode(6)

    Solution().reverseBetween(node, 1,1)



