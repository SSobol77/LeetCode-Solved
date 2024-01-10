# 59. Spiral Matrix II

# Topic:  Array, Matrix, Simulation

'''
# Task:
--------
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20

# Testcase:
---------------
3
1

# Code:
--------
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
     
'''
# Solution:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix filled with zeros.
        matrix = [[0] * n for _ in range(n)]

        # Initialize starting position and direction.
        # row, col: current position in the matrix.
        # dRow, dCol: direction of movement, initially set to move right.
        row, col, dRow, dCol = 0, 0, 0, 1

        # Iterate over the numbers from 1 to n^2.
        for num in range(1, n*n + 1):
            # Fill the current cell with the current number.
            matrix[row][col] = num

            # Check if the next step is either out of bounds or into a filled cell.
            # (row + dRow) % n and (col + dCol) % n wrap around to ensure we stay within bounds.
            if matrix[(row + dRow) % n][(col + dCol) % n]:
                # Change direction: turn right by swapping dRow and dCol and negating dCol.
                dRow, dCol = dCol, -dRow

            # Move to the next cell in the current direction.
            row += dRow
            col += dCol

        # Return the filled spiral matrix.
        return matrix


# Tests:
sol = Solution()
print(sol.generateMatrix(3))  # Output: [[1,2,3],[8,9,4],[7,6,5]]
print(sol.generateMatrix(1))  # Output: [[1]]

# Description:
'''
The generateMatrix function in the Solution class generates an n×n matrix filled with numbers from 1 to n^2 in a spiral order.
The spiral starts from the top-left corner of the matrix and moves initially to the right.

1. Matrix Initialization: The matrix is initially filled with zeros, representing empty cells.

2. Starting Position and Direction: The algorithm starts at the top-left corner (0,0) of the matrix. The initial direction is set to move right.

3. Filling the Matrix: The matrix is filled with numbers from 1 to n^2. The filling process continues in the current direction until it encounters 
either the edge of the matrix or a cell that has already been filled.

4. Direction Change: Whenever the algorithm encounters a boundary or a filled cell, it changes direction in a clockwise manner (right turn). This 
is done by swapping the row and column increments and negating the column increment. This ensures the spiral pattern.

5. Completion: The process repeats until all cells are filled. The algorithm ensures that the filling process follows a spiral path from the 
outer layer towards the center.

6. Output: The function returns the completed spiral matrix.

This implementation is efficient, as it minimizes checks for boundaries and filled cells, relying on a predictable pattern and mathematical 
properties to ensure the spiral pattern is maintained.

'''
