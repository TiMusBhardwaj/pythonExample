# https://leetcode.com/problems/product-of-array-except-self/solution/
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        #ans = []
        temp =1
        for index, num in enumerate(nums):
            left.append(temp * nums[index])
            temp = temp * nums[index]
        temp=1
        for index in range(len(nums)-1,-1,-1):
            if index == 0:
                left [index] = temp
            else :
                left[index] = temp*left[index-1]
            temp = temp * nums[index]


        return left

if __name__ == '__main__':
    Solution().productExceptSelf([1,2,3,4])