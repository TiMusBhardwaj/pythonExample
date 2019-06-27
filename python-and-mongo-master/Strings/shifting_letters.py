from typing import List
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        arr = list(S)
        sum = 0
        index = len(shifts)-1
        while index >=0:
            sum += shifts[index]
            temp = (ord(S[index]) - 97 + sum) % 26
            arr[index] = chr(temp + 97)
            index -=1

        return "".join(arr)

if __name__ == '__main__':
    print(Solution().shiftingLetters("abc", [3,5,9]))