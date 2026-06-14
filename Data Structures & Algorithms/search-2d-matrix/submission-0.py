class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            m = matrix[r][c]
            if m > target:
                c -= 1
            elif m < target:
                r += 1
            else:
                return True
        return False