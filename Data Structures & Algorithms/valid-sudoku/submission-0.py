class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        box = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                digit_idx = int(board[r][c]) - 1
                box_idx = (r//3) * 3 + (c // 3)
                if (rows[r][digit_idx] or
                    cols[c][digit_idx] or
                    box[box_idx][digit_idx]):
                    return False
                rows[r][digit_idx] = True
                cols[c][digit_idx] = True
                box[box_idx][digit_idx] = True
        return True

