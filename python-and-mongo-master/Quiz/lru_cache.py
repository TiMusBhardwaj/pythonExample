from Quiz.DoublyLinkedList import DoublyLinkedList
from Quiz.DoublyLinkedList import Node

class LRUCache:


    def __init__(self, capacity: int):
        self.list = DoublyLinkedList()
        self.capacity = capacity
        self.size = 0
        self.map = {}

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        else:
            self.list.remove_node_lru(node)
            self.list.prepend(node)
        return node.value

    def put(self, key: int, value: int):
        #node = Node(value)
        node = self.map.get(key)
        if node is None:
            if len(self.map) == self.capacity:
                node = self.list.remove_node_from_end()
                self.map.pop(node.key)
            node = Node(value, key)
            self.list.prepend(node)
            self.map[key]=node
        else :
            node.value = value
            self.list.remove_node(node)
            self.list.prepend(node)

        #res = self.map.get(key)
        #if res is not None:

if __name__ == '__main__':

    cache = LRUCache(2);

    cache.put(1, 1);
    cache.put(2, 2);
    print(cache.get(1))   # returns    1
    cache.put(3, 3); # evicts  key   2
    print(cache.get(2)) # returns - 1(not found)
    cache.put(4, 4); # evicts  key   1
    print(cache.get(1)) # returns - 1(not found)
    print(cache.get(3)) # returns   3
    print(cache.get(4)) # returns     4



