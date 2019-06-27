#https://leetcode.com/problems/permutations/
from typing import List
class Solution:
    def __init__(self):
        self.result = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.permute_helper([],sorted(nums))
        return self.result

    def permute_helper(self, fixed, nums):
        if len(nums) ==0:
            self.result.append(fixed)
            return

        for index, num in enumerate(nums):
            if index ==0 or num != nums[index-1]:
                temp = fixed[:]
                temp.append(num)
                self.permute_helper(temp,nums[:index]+nums[index+1:])
        return
if __name__ == '__main__':
    res = Solution().permuteUnique([3,3,0,3])
    print(res)