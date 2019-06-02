class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        length = len(nums)
        for index in range(0, length-1):
            count = 1
            while count <= k and index+count <= length -1:
                if abs(nums[index] - nums[index + count]) <= t:
                    return True
                count +=1
        return False

if __name__ == '__main__':
    print(Solution().containsNearbyAlmostDuplicate([2,2],3,0))