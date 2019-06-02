'''
Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
    /
   4
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges):

        if n == 0:
            return None
        if n==1 :
            return [0]
        if n==2:
            return [edges[0][0], edges[0][1]]

        arr=[[] for _ in range(n)]
        for edge in edges:
            arr[edge[0]].append(edge[1])
            arr[edge[1]].append(edge[0])


        leaves = []
        for index in range(0, len(arr)):
            if len(arr[index]) ==1:
                leaves.append(index)

         #remove leaves
        while n>2:
            n-=len(leaves)
            new_leaves = []
            for leaf in leaves:
                connected_leaves = arr[leaf]
                arr[leaf] =[]
                for connected_leaf in connected_leaves:
                    arr[connected_leaf].remove(leaf)
                    if len(arr[connected_leaf]) ==1:
                        new_leaves.append(connected_leaf)
            leaves = new_leaves
        return leaves


if __name__ == '__main__':
    print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))