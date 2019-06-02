class Solution(object):

    def __init__(self):
        self.inc1 = [1, 0, 0 , -1]
        self.inc2 = [0, 1, -1, 0]


    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.lengthX = len(grid)
        self.lengthY = len(grid[0])

        res  = 0
        for i in range(0, self.lengthX):
            for j in range(0, self.lengthY):
                if grid[i][j] == 1:
                    res = max(self.cover_island( i, j, grid), res)
        return res


    def cover_island(self, i, j, grid):
        grid[i][j] = -1
        count = 1
        for a, b in zip(self.inc1, self.inc2):
            if i+a >=0  and i+a < self.lengthX and j+b >=0  and j+b < self.lengthY and grid[i+a][j+b] == 1:
                count =  self.cover_island(i+a, j+b, grid) +count
        return count


if __name__ == '__main__':
    Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]])