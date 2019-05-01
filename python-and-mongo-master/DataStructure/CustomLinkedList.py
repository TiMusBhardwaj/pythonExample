from DataStructure.LinkedListNode import Node


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def sortedInsert(self, newNode):
        if self.head is None:
            self.head = newNode
            return

        elif self.head.data >= newNode.data:
            newNode.next = self.head
            self.head = newNode
        else :
            current = self.head
            while current.next is not None and current.next.data < newNode.data:
                current = current.next

            newNode.next = current.next
            current.next = newNode

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def deleteNode(self, node):
        if self.head is None:
             return
        elif self.head == node:
            self.head = None
            return
        else :
            current = self.head
            while current.next is not None:
                if current.next == node:
                    current.next = current.next.next
                current = current.next


if __name__ == '__main__':
    llist = LinkedList()
    new_node = Node(5)
    llist.sortedInsert(new_node)
    new_node = Node(10)
    llist.sortedInsert(new_node)
    new_node = Node(7)
    llist.sortedInsert(new_node)
    new_node = Node(3)
    llist.sortedInsert(new_node)
    new_node = Node(1)
    llist.sortedInsert(new_node)
    new_node = Node(9)
    llist.sortedInsert(new_node)
    print
    "Create Linked List"
    llist.printList()
    llist.deleteNode(new_node)
    llist.printList()
