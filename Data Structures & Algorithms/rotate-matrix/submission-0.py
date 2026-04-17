class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        sizeN = len(matrix)
        for i in range(sizeN-1, -1, -1):
            for j in range(sizeN):
                matrix[j].append(matrix[i][j])


        for i in range(sizeN):
            for j in range(sizeN):
                matrix[i].remove(matrix[i][0])

        print(matrix)
        
