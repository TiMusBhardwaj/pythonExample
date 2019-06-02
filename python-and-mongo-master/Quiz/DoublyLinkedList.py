class Node(object):
    def __init__(self, val, key):
        self.value = val
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, node):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        node.next = self.head
        if node.next is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def add_node(self, val):
        new_node = Node(val)
        # If no head, set new node as head
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            current_node = self.head
            # if next not none (tail) continue traversing
            while current_node.next != None:
                current_node = current_node.next
            # if tail, add to end
            current_node.next = new_node
            # set prev pointer to current node
            new_node.prev = current_node
            # set new tail to new node
            self.tail = new_node


    def remove_node_lru(self, node):
        if node is None:
            return node

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.next, node.prev = None, None
        return node


    def remove_node_from_end(self):
        if self.head != None:
            current_node = self.head
            while current_node.next.next != None:
                current_node = current_node.next
            del_node = current_node.next
            current_node.next.prev = None
            current_node.next = None
            self.tail = current_node
            return del_node

    def remove_node(self, val):
        if self.head != None:
            current_node = self.head
            # If val is the head
            if self.head.value == val:
                self.head.next.prev = None
                self.head = self.head.next
            # If val is the tail
            elif self.tail.value == val:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                while current_node.next.value != val:
                    current_node = current_node.next
                    # If val is not in list
                    if current_node.next.value != val:

                        return False
                # Set next next node's prev pointer to current node
                current_node.next.next.prev = current_node
                # Set next node to current's next next pointer
                current_node.next = current_node.next.next

    def insert_node_after(self, val, insert_val):
        if self.head != None:
            # Create new node
            current_node = self.head
            new_node = Node(insert_val)
            # If val is first item in list, insert after
            if self.head.value == val:
                self.head.next.prev = new_node
                new_node.prev = self.head
                new_node.next = self.head.next
                self.head.next = new_node
            # If tail is val, create new tail
            elif self.tail.value == val:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                # If neither head nor tail, traverse through
                while current_node.value != val:
                    current_node = current_node.next
                    # If val is not in list, give error message
                    if current_node.value != val:

                        return False
                # Set new node's next to current node's next
                new_node.next = current_node.next
                # Insert new node next to current node
                current_node.next = new_node
                # Set new node next prev's pointer to new node
                new_node.next.prev = new_node
                # Set new node's prev pointer to current node
                new_node.prev = current_node

