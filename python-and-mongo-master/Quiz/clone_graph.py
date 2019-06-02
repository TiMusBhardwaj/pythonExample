
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    def __repr__(self):
        return str(self.val)



class Solution:
    def __init__(self):
        self.map = {}


    def cloneGraph(self, node) -> Node:
        node_copy = self.map.get(node)
        if node_copy is None:
            node_copy = Node(node.val, None)
            self.map[node] = node_copy
            neigh = []
            for node_neighbor in node.neighbors:
                neigh.append(self.cloneGraph(node_neighbor))
            node_copy.neighbors = neigh


        return node_copy


if __name__ == '__main__':
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    node = Solution().cloneGraph(node1)
    print(node == node1)
    print(node)



