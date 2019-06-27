from functools import reduce
import itertools


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return  self.arr2("", sorted(list(tiles)))
    def arr(self, fixed, lst):
        #print(str(lst))
        ans =1
        res = []
        for (index, char) in enumerate(lst):
            if index ==0 or lst[index -1] != char:
                print(char + "".join(lst[:index] +lst[index+1:]))
                ans += self.arr(fixed + char , lst[:index] +lst[index+1:])
                print()
        return ans

    def arr2(self, fixed, lst):
        if len(lst) == 0:
            return 1,[""]
        ans =1
        res = []
        for (index, char) in enumerate(lst):
            if index ==0 or lst[index -1] != char:
                count, ar = self.arr2(fixed + char , lst[:index] +lst[index+1:])
                ans += count
                for x in ar:
                    print(char+x)
                    res.append(char+x)
        return ans,res


def arrangements (lst):
    ans = 1
    for (index, char) in enumerate (lst):
        if index == 0 or lst[index-1] != char:
            ans += arrangements (lst[:index] + lst[index+1:])
    return ans

class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        return arrangements (sorted ([ch for ch in tiles])) - 1

if __name__ == '__main__':
    res = Solution().numTilePossibilities("ABC")
    print(res)