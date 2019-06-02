class Solution:
    def __init__(self):
        self.map = {}

    def numDecodings2(self, s: str):
        if self.map.get(s) is not None:
            return  self.map.get(s)
        length = len(s)
        if length == 0:
            return 1
        if length == 1 and s[0] is '0':
            return 0
        elif length == 1:
            return 1

        char1 = int(s[0])
        char2 = int(s[1])

        if (char1 > 0 and char1 < 2) or (char1 ==2 and char2 <= 6):
            temp_res = self.numDecodings(s[1:]) + self.numDecodings(s[2:])
            self.map[s] = temp_res
            return temp_res
        else:
            temp_res =  self.numDecodings(s[1:])
            self.map[s] = temp_res
            return temp_res

    def numDecodings(self, s: str):
        if s.startswith('0'):
            return 0
        else:
            return self.numDecodings2(s)


if __name__ == '__main__':
    print(Solution().numDecodings("10"))