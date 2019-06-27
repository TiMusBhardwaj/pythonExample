class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows ==1:
            return s
        res = [""]*numRows
        curr_row =0
        going_down = False
        for x in s:
            res[curr_row] +=x
            if curr_row ==0 or curr_row == numRows -1:
                going_down = not going_down
            curr_row += 1 if going_down else -1

        return "".join(res)


if __name__ == '__main__':
    Solution().convert("AB",2)