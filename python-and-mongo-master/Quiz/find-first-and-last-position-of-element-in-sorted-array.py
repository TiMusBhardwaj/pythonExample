class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findFirst(nums, target), self.findLast(nums, target)]


    def findFirst(self, nums, target):

        start = 0
        end = len(nums) -1

        while start <= end:
            mid = int((start + end)/2)
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    end = mid-1
            elif nums[mid] > target :
                end = mid-1
            else:
                start = mid+1
        return -1

    def findLast(self, nums, target):

        start = 0
        end = len(nums) -1

        while start <= end:
            mid = int((start + end)/2)
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid + 1] > target:
                    return mid
                else:
                    start = mid+1
            elif nums[mid] > target :
                end = mid-1
            else:
                start = mid+1
        return -1

if __name__ == '__main__':
    print(Solution().searchRange([1,2,3,4,5,6,6,6,7,8], 6))