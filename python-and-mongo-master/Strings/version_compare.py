import itertools as it
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split('.')

        for x1, x2 in it.zip_longest(arr1, arr2):

            x1 = 0 if x1 is None else int(x1)
            x2 = 0 if x2 is None else int(x2)

            if x1 > x2:
                return 1
            if x1 < x2:
                return -1
            else:
                continue
        return 0


if __name__ == '__main__':
    Solution().compareVersion("0.1", "1.1")
   