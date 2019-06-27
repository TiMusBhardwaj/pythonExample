# https://leetcode.com/problems/container-with-most-water/
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start =0
        end = len(height)-1
        max_water =0

        while start < end:
            max_water = max(max_water , (end-start)*min(height[start], height[end]))
            if height[start]> height[end]:
                end=end-1
            else:
                start = start+1
        return max_water


if __name__ == '__main__':
    Solution().maxArea([1,8,6,2,5,4,8,3,7])
