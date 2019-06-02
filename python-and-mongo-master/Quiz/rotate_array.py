class Solution:
    def rotate(self, nums, k: int) -> None:

        if k >= len(nums):
            k = k%len(nums)
        remainder = len(nums)%k
        if k == 0 or len(nums) ==1:
            return
        for index in range(len(nums)-1, remainder+k-1, -1):
            nums[index], nums[index-k] = nums[index-k], nums[index]
        for index in range (remainder, remainder+k):
            nums[index], nums[index - remainder] = nums[index - remainder], nums[index]


        return nums
if __name__ == '__main__':
    print(Solution().rotate([1,2,3,4,5,6,7,8], 3))


