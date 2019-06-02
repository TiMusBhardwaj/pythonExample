class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int):
        if root is None:
            return [None]*k
        node = root
        length =1
        while node.next is not None:
            node = node.next
            length +=1
        subset_major = int(length/k)
        subset_minor = length%k
        node = root
        res = [None]*k

        for index in range(0, k):
            res[index] = node
            size = subset_major
            if subset_minor >0:
                subset_minor -=1
                size += 1
            while size >1:
                node = node.next
                size -=1
            if node is not None:
                node.next, node = None, node.next
        return res


if __name__ == '__main__':
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    #node.next.next.next.next = ListNode(5)
    Solution().splitListToParts(node,5)
