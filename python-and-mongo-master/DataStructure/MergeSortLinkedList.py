from DataStructure.CustomLinkedList import LinkedList as list


class LinkedList(list):

    def middleNode(self, head):
        slow, fast = head, head

        if head.next and head.next.next is None:
            part2 = head.next
            head.next = None
            return head, part2

        while slow and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        part2 = slow.next
        slow.next = None

        return head, part2

    def mergeSort(self, node):
        if node.next is None:
            return node

        head1, head2 = self.middleNode(node)
        head1 = self.mergeSort(head1)
        head2 = self.mergeSort(head2)
        temp = LinkedList()
        node1 = head1
        node2 = head2
        head = None
        if node1.data > node2.data:
            head = node2
            node2 = node2.next
        else:
            head = node1
            node1 = node1.next
        curr = head
        while node1 and node2:
            if node1.data > node2.data:
                curr.next = node2
                curr = node2
                node2 = node2.next
            else:
                curr.next = node1
                curr = node1
                node1 = node1.next

        while node1:
            curr.next = node1
            curr = node1
            node1 = node1.next

        while node2:
            curr.next = node2
            curr = node2
            node2 = node2.next

        return head








if __name__ == '__main__':
    llist = LinkedList()
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(61)
    llist.push(5)
    llist.push(4)

    llist2.head = llist.mergeSort(llist.head)
    llist2.printList()


