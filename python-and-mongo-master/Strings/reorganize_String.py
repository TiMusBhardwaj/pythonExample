# https://leetcode.com/problems/reorganize-string/solution/
from queue import PriorityQueue
class Solution:
    def reorganizeString(self, S: str) -> str:
        arr = [0]*26
        intA = ord('a')
        for ch in S:
            arr[ord(ch) - intA] = arr[ord(ch) - intA] + 1
        q = PriorityQueue()
        for count,index in enumerate(arr):
            if count !=0:
                q.put(count, chr(index+intA))
        while not q.empty():
            next_item = q.get()
            print(next_item)
        print(q)

if __name__ == '__main__':
    Solution().reorganizeString("aaab")