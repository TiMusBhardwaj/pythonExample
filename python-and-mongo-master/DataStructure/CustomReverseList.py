from DataStructure.CustomLinkedList import LinkedList as list

#https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
class LinkedList(list):

    def reverse(self, node, k):
        count = 0
        curr = node
        prev = None
        next = None

        while k > count and curr is not None:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
            next = nextnode
            count += 1

        if next is not None:
            node.next = self.reverse(next, k)

        return prev

    def reverseList(self, head):
        curr = head
        prev = None
        nextnode = None

        while curr is not None:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode

        return prev




if __name__ == '__main__':
    llist = LinkedList()
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Given linked list")
    llist.printList()
    head = llist.head
    llist.head = llist.reverse(head,3)

    print("\nReversed Linked list")
    llist.printList()