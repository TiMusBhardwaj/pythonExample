from DataStructure.CustomLinkedList import LinkedList as list


class LinkedList(list):

    def merge(self, q):
        p_curr = self.head
        q_curr = q.head
        while p_curr is not None and q_curr is not None:
            p_next = p_curr.next
            q_next = q_curr.next

            p_curr.next = q_curr
            q_curr.next=p_next

            p_curr =p_next
            q_curr=q_next

        q.head = q_curr


if __name__ == '__main__':
    # Driver program to test above functions
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.push(3)
    llist1.push(2)
    llist1.push(1)

    print("First Linked List:")
    llist1.printList()

    llist2.push(8)
    llist2.push(7)
    llist2.push(6)
    llist2.push(5)
    llist2.push(4)

    print("Second Linked List:")

    llist2.printList()
    llist1.merge(llist2)

    print("Modified first linked list:")
    llist1.printList()

    print("Modified second linked list:")
    llist2.printList()
