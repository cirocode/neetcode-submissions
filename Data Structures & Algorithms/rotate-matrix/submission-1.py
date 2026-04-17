class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)

        for i in range(size):
            for j in range(i + 1, size):
                prev = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = prev
        for i in range(size):
            matrix[i].reverse()
        
