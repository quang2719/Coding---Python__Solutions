class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False for _ in range(n)]
        rows = [False for _ in range(n)]
        def backTrack(table, rows, cols, i)