# https://leetcode.com/problems/trapping-rain-water/solution/
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0

        left_max =height[0]
        right_max=height[-1]

        left =0
        right =len(height)-1
        while left < right:
            if left_max > right_max:
                if right_max > height[right-1]:
                    ans += right_max - height[right-1]
                else:
                    right_max = height[right-1]
                right = right-1
            else:
                if left_max > height[left+1]:
                    ans += left_max - height[left+1]
                else:
                    left_max = height[left+1]
                left = left+1
        return ans

if __name__ == '__main__':
    res = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(res)