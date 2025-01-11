from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==1:
            return [['Q']]
        
        used_cols = [False for _ in range(n+1)]
        diagonal1 = [False for _ in range(n*2)]
        diagonal2 = [False for _ in range(n*2)]
        res = []
        table = [0 for _ in range(n+1)]
        
        def backTrack(table, res, cur_row,diagonal1,diagonal2,used_cols,n):
            if cur_row > n:
                res.append(table.copy())
                return
            for col in range(1,n+1):
                # calculate id1 id2
                # id 1
                id1 = cur_row - col + n
                # id 2
                id2 = cur_row + (col-1)
                if(
                    not used_cols[col] and
                    not diagonal1[id1] and
                    not diagonal2[id2]
                ):
                    used_cols[col] = True
                    diagonal1[id1] = True
                    diagonal2[id2] = True
                    table[cur_row] = col
                    backTrack(table,res,cur_row+1,diagonal1,diagonal2,used_cols,n)
                    used_cols[col] = False
                    diagonal1[id1] = False
                    diagonal2[id2] = False


        backTrack(table,res,1,diagonal1,diagonal2,used_cols,n)
        ans = []
        for tabel in res:
            board = [['.' for _ in range(n)] for _ in range(n)]
            for row,col in enumerate(tabel):
                if row >0:
                    board[row-1][col-1] = 'Q'
            formated_board = [''.join(x) for x in board]
            ans.append(formated_board)
        return ans


solution = Solution()

# Trường hợp kiểm thử 1
n = 1
print(n)
print(solution.solveNQueens(n))  # Output: [['Q']]

# Trường hợp kiểm thử 2
n = 2
print(n)

print(solution.solveNQueens(n))  
n = 3
print(n)

print(solution.solveNQueens(n))  
n = 4
print(n)

print(solution.solveNQueens(n))  

n = 5
print(n)
print(solution.solveNQueens(n))  

