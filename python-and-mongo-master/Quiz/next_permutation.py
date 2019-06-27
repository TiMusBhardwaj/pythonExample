#https://leetcode.com/problems/next-permutation/

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums)-1, 0, -1):
            if nums[index] >nums[index-1]:
                for index_temp in range (len(nums)-1, 0, -1):
                    if nums[index_temp] > nums[index-1]:
                        nums[index_temp], nums[index-1] = nums[index -1], nums[index_temp]
                        break
                #reverse rest of array:
                start = index
                end = len(nums)-1
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start +=1
                    end-=1
                return

        else:
            start = 0
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return

if __name__ == '__main__':
    Solution().nextPermutation([3,2,1])




