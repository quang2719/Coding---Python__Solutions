from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def travel(cur_state, availabel_state, target, grid, i):
            if i == len(target) - 1:
                return True
            cur_row, cur_col = cur_state

            # left
            new_col = cur_col - 1
            new_row = cur_row
            if (
                new_col >= 0 and
                availabel_state[new_row][new_col] and
                target[i + 1] == grid[cur_row][new_col]
            ):
                availabel_state[new_row][new_col] = False
                res1 = travel(
                    (new_row, new_col),
                    availabel_state,
                    target,
                    grid,
                    i + 1
                )
                availabel_state[new_row][new_col] = True
                if res1:
                    return True

            # right
            new_col = cur_col + 1
            new_row = cur_row
            if (
                new_col < len(grid[0]) and
                availabel_state[new_row][new_col] and
                target[i + 1] == grid[cur_row][new_col]
            ):
                availabel_state[new_row][new_col] = False
                res2 = travel(
                    (new_row, new_col),
                    availabel_state,
                    target,
                    grid,
                    i + 1
                )
                availabel_state[new_row][new_col] = True
                if res2:
                    return True

            # up
            new_col = cur_col
            new_row = cur_row - 1
            if (
                new_row >= 0 and
                availabel_state[new_row][new_col] and
                target[i + 1] == grid[new_row][new_col]
            ):
                availabel_state[new_row][new_col] = False
                res3 = travel(
                    (new_row, new_col),
                    availabel_state,
                    target,
                    grid,
                    i + 1
                )
                availabel_state[new_row][new_col] = True
                if res3:
                    return True

            # down
            new_col = cur_col
            new_row = cur_row + 1
            if (
                new_row < len(grid) and
                availabel_state[new_row][new_col] and
                target[i + 1] == grid[new_row][new_col]
            ):
                availabel_state[new_row][new_col] = False
                res4 = travel(
                    (new_row, new_col),
                    availabel_state,
                    target,
                    grid,
                    i + 1
                )
                availabel_state[new_row][new_col] = True
                if res4:
                    return True

            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    availabel_state = [[True for _ in range(len(board[0]))] for _ in range(len(board))]
                    availabel_state[row][col] = False
                    if travel((row, col), availabel_state, word, board, 0):
                        return True
        return False
