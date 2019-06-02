# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


def is_palindrome(head_s, head_l):
    if head_l is None:
        return True,head_s

    is_palindrome_var, head_s = is_palindrome(head_s, head_l.next)
    if not is_palindrome_var:
        return False,None

    if head_s.data == head_l.data:
        return True, head_s.next
    else :
        return False, None

if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(2)
    node.next.next.next.next = Node(1)
    print(is_palindrome(node, node))
    node.next.next.next = Node(3)
    print(is_palindrome(node, node))

