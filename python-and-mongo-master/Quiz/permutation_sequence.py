#https://leetcode.com/problems/permutation-sequence/

class Solution:
    def __init__(self):

        self.result = 
    def getPermutation(self, n: int, k: int) -> str:


        def permute_helper(self, fixed, nums):
            if len(nums) == 0:
                count -=1
                self.result.append(fixed)
                return

            for index, num in enumerate(nums):
                if index == 0 or num != nums[index - 1]:
                    temp = fixed[:]
                    temp.append(num)
                    self.permute_helper(temp, nums[:index] + nums[index + 1:])
            return