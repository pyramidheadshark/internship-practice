### Optimal
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for y in range(n):
            for x in range(y):
                matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
            
        for y in range(n):
            for x in range(n // 2):
                matrix[y][x], matrix[y][n - x - 1] = matrix[y][n - x - 1], matrix[y][x]
        
        return matrix