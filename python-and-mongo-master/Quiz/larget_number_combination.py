class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        mapping = map(str, nums)
        temp = sorted(mapping, key=LargerNumKey)
        largest_num = ''.join(temp)
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':

    res  = Solution().largestNumber([3,30,34,5,9])
    print(res)
    print ('20' > '30')