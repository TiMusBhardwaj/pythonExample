# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def pair_swap(self):
        root = self.head
        if not root or not root.next:
            return root
        prev = None
        first = root
        second = root.next

        while first and second:

            #SwAp
            if prev:
                prev.next = second
            else:
                self.head = second
            first.next = second.next
            second.next = first

            #MOve Pointer Ahead
            prev = first
            if first.next and first.next.next:
                second = first.next.next
                first = first.next
            else:
                break

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,)
            temp = temp.next

if __name__ == '__main__':
    # Driver program
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)

    print("Linked list before calling pairWiseSwap() ")
    llist.printList()

    llist.pair_swap()

    print("\nLinked list after calling pairWiseSwap()")
    llist.printList()
