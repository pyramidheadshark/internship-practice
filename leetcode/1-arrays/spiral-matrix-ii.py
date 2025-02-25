### Optimal
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)] 
        current = 1

        top_row = 0
        bot_row = n - 1
        left_col = 0
        right_col = n - 1

        while top_row <= bot_row and left_col <= right_col:
            for col in range(left_col, right_col + 1):
                matrix[top_row][col] = current
                current += 1
            top_row += 1

            for row in range(top_row, bot_row + 1):
                matrix[row][right_col] = current
                current += 1
            right_col -= 1

            for col in range(right_col, left_col - 1, -1):
                matrix[bot_row][col] = current
                current += 1
            bot_row -= 1

            for row in range(bot_row, top_row - 1, -1):
                matrix[row][left_col] = current
                current += 1
            left_col += 1
        
        return matrix