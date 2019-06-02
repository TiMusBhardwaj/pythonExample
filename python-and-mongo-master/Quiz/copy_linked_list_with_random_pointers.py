
# Definition for a Node.
class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
    def __repr__(self):
        return str(self.val) + ': random ->' + ("None" if self.random is None else str(self.random.val)) \
                                                                                  + ': next -> ' + ("None" if self.next is None else str(self.next.val))


class Solution:

    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Node') -> 'Node':

        #head_copy = Node(head.val, None, None)
        arr = [head]
        #map[head] = head_copy
        #map ={}
        while len(arr)>0:
            node = arr.pop(0)
            copy_node = self.map.get(node)
            if copy_node is None:
                copy_node = Node(head.val, None, None)
                self.map[node] = copy_node
            if node.next is not None:
                copy_node_next = self.map.get(node.next)
                if copy_node_next is None:
                    copy_node_next = Node(node.next.val)
                    arr.append(node.next)
                    self.map[node.next] = copy_node_next
                copy_node.next = copy_node_next

            if node.random is not None:
                copy_node_random = self.map.get(node.random)
                if copy_node_random is None:
                    copy_node_random = Node(node.random.val)
                    arr.append(node.random)
                    self.map[node.random] = copy_node_random
                copy_node.random = copy_node_random
        return self.map.get(head)



if __name__ == '__main__':
    node = Node(1)
    node.next = Node(2)
    node.next.next = Node(3)
    node.next.next.next = Node(4)
    node.next.next.next.next = Node(5)

    node.next.random = node.next.next.next.next
    node.next.next.random = node
    node.random = node.next.next.next.next
    node.next.next.next.random = node.next.next.next

    Solution().copyRandomList(node)