# 221. Maximal Square.

# Topic: Array, Dynamic Programming, Matrix.

'''
# Task:
-------
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.


# Testcase:
-----------
[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
[["0","1"],["1","0"]]
[["0"]]


# Code:
-----------
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

'''
# Solution:
class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            # If the matrix is empty, return 0 as there can be no squares
            return 0

        m, n = len(matrix), len(matrix[0])
        # Initialize a DP table with dimensions of the matrix filled with zeros
        dp = [[0] * n for _ in range(m)]
        max_side = 0  # Variable to track the maximum side length of the square found

        for i in range(m):
            for j in range(n):
                # Check if the current cell contains '1'
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        # If it's the first row or column, the largest square can only be 1x1
                        dp[i][j] = 1
                    else:
                        # Calculate the size of the largest square that can be formed at cell (i, j)
                        # It is limited by the smallest of the three neighboring cells: to the left, above, and diagonally left
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # Update the maximum side length found so far
                    max_side = max(max_side, dp[i][j])

        # The area of the largest square is the square of the maximum side length
        return max_side ** 2

# Testcases
sol = Solution()
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  # Output: 4
print(sol.maximalSquare([["0","1"],["1","0"]]))  # Output: 1
print(sol.maximalSquare([["0"]]))  # Output: 0


# Description:
'''
In this implementation:

    We start by checking if the input matrix is empty. If so, we immediately return 0 because no squares can be formed in an empty matrix.
    We create a DP table dp with the same dimensions as the input matrix. Each cell in dp will store the side length of the largest square with its bottom-right corner at the corresponding cell in the input matrix.
    We iterate over each cell in the input matrix. If a cell contains a "1", we calculate the largest square that can be formed with that cell as the bottom-right corner. This calculation is based on the minimum side length of squares formed by its neighboring cells (above, to the left, and diagonally up-left) plus 1.
    We update the max_side variable if we find a square with a larger side length than previously recorded.
    Finally, we return the area of the largest square found, which is the square of the max_side.

'''
