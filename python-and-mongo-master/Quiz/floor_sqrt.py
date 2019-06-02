class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        start = 1
        end = x/2+1
        res = None
        while start <= end:
            mid = int((start + end) / 2)
            if mid*mid == x:
                return mid
            if mid *mid < x:
                res = mid
                start = mid+1
            else :
                end = mid-1
        return res

if __name__ == '__main__':
    print(Solution().mySqrt(8))