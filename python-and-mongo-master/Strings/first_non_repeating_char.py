class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr = [-1]*26
        index =0
        for x in s:
            t_index =ord(x)%26
            if arr[t_index%26] ==-1:
                arr[t_index] = index
            else:
                arr[t_index] = -2

            index+=1

        print(list(filter(lambda x: x >=0 , arr)))
        return min(list(filter(lambda x: x >=0 , arr)))


if __name__ == '__main__':
    Solution().firstUniqChar("leetcode")