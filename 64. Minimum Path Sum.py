# 64. Minimum Path Sum.

# Topic: Array, Dynamic Programming, Matrix.

'''
# Task:
-----------
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which 
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

# Testcase:
------------------
[[1,3,1],[1,5,1],[4,2,1]]
[[1,2,3],[4,5,6]]

# Code:
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      
'''
# Solution:
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]  # Starting point
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]  # Top row
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]  # Leftmost column
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]  # Other cells

        return dp[m-1][n-1]

# Testcases
sol = Solution()
print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7
print(sol.minPathSum([[1,2,3],[4,5,6]]))  # Output: 12


# Description 
'''
To solve this problem, we will use Dynamic Programming (DP), which is a common technique for problems 
like this where we need to find an optimal solution based on decisions made at each step.

We will create a DP table of the same size as the grid and fill it with the minimum sum needed to reach 
each cell. The minimum sum to reach a cell is the value of the cell plus the minimum of the sums needed
to reach the cells above and to the left of it. The top-left cell is the starting point, so its minimum 
sum is its own value. For the cells in the top row and leftmost column, we only add the value of the 
previous cell in the respective row or column since there's only one way to reach them.

In this code:
- We first check if the grid is empty.
- m and n are the dimensions of the grid.
- dp is the DP table initialized with zeroes.
- We iterate over each cell in the grid, filling in the dp table with the minimum sum to reach that cell.
- The final answer is the value in the bottom-right cell of the dp table, which represents the minimum 
path sum to reach that point from the top-left corner.

'''