class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        live cell:
            fewer than 2 live -> die
            2 or 3 live -> live
            greater than 3 live -> die
        dead cell:
            exactly 3 live -> live
        """
        m = len(board) #row
        n = len(board[0]) # col
        res = [[board[i][j] for j in range(n)] for i in range(m)]

        for row in range(m):
            for col in range(n):
                cell = board[row][col]
                cell_u = board[row-1][col] if row > 0 else 0
                cell_d = board[row+1][col] if row < m-1 else 0 
                cell_l = board[row][col-1] if col > 0 else 0
                cell_r = board[row][col+1] if col < n -1 else 0
                cell_ru = board[row-1][col+1] if ((row >0 and col < n-1)) else 0
                cell_lu = board[row-1][col-1] if ((row >0 and col >0)) else 0
                cell_rd = board[row+1][col+1] if ((row < m-1 and col < n-1)) else 0
                cell_ld = board[row+1][col-1] if ((row < m-1 and col > 0)) else 0

                total_live_nb = cell_u+cell_d+cell_l+cell_r+cell_lu+cell_ld+cell_rd+cell_ru
                if cell == 1:
                    if total_live_nb <2: res[row][col] = 0
                    elif total_live_nb ==2 or total_live_nb ==3:
                        res[row][col] = 1
                    else: res[row][col] = 0
                else:
                    if total_live_nb == 3:
                        res[row][col] = 1
        for i in range(m):
            for j in range(n):
                board [i][j]= res[i][j]
                    
                
