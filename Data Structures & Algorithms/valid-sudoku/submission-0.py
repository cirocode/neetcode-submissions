class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Checks Rows

        for row in board:
            seen_in_row = []
            for column in row:
                if column != ".":
                    if column in seen_in_row:
                        return False
                    else:
                        seen_in_row.append(column)

        # Check Columns
        for i in range(9):
            seen_in_column = []
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen_in_column:
                    return False
                seen_in_column.append(board[j][i])


        # Check 3x3 Squares
        for square in range(9):
            seen_in_sub = []
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen_in_sub:
                        return False
                    seen_in_sub.append(board[row][col])


        return True