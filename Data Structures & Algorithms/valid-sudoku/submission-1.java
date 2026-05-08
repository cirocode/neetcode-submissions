class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Check row
        List<Character> seen = new ArrayList<>();

        for (int row = 0; row < 9; row++) {
            seen.clear();
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') {
                    continue;
                }
                if (seen.contains(board[row][col])) {
                    return false;
                } else {
                    seen.add(board[row][col]);
                }
            }
        }

        // Check Columns
        for (int row = 0; row < 9; row++) {
            seen.clear();
            for (int col = 0; col < 9; col++) {
                if (board[col][row] == '.') {
                    continue;
                }
                if (seen.contains(board[col][row])) {
                    return false;
                } else {
                    seen.add(board[col][row]);
                }
            }
        }

        // Check 3x3 squares
        for (int square = 0; square < 9; square++) {
            seen.clear();

            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;

                    if (board[row][col] == '.') {
                        continue;
                    }

                    if (seen.contains(board[row][col])) {
                        return false;
                    } else {
                        seen.add(board[row][col]);
                    }
                }
            }
        }

        return true;
    }
}
