class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for index in range (1, len(board)-1):
            arr = board[index]
            for ch in range(1, len(arr)-1):
                if arr[ch] is 'O':
                    safe = True
                    if ch-1 == 0 and arr[ch-1] is 'O':
                        safe = False
                    if ch +1 == len(arr)-1 and arr[ch+1] is 'O':
                        safe = False
                    if index -1 == 0 and board[index-1][ch] is 'O':
                        safe = False
                    if index + 1 == len(board)-1 and board[index + 1][ch] is 'O':
                        safe = False
                    if safe:
                        arr[ch] = 'X'