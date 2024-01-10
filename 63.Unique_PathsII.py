# 63. Unique Paths II.

# Topic: Array, Dynamic Programming, Matrix.


'''
# Task:
--------------
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square 
that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 10^9.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.


# Testcase:
--------------
[[0,0,0],[0,1,0],[0,0,0]]
[[0,1],[0,0]]


# Code:
--------------
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    
'''

# Solution:
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        # Check if the starting point is an obstacle or the grid is empty
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        # Get the dimensions of the grid
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Initialize DP table with zeros
        dp = [[0] * n for _ in range(m)]

        # Starting point
        dp[0][0] = 1

        # Initialize the first column of the DP table
        # If there is an obstacle, all cells below it in the same column are unreachable
        for i in range(1, m):
            dp[i][0] = int(dp[i-1][0] == 1 and obstacleGrid[i][0] == 0)
        
        # Initialize the first row of the DP table
        # If there is an obstacle, all cells to the right of it in the same row are unreachable
        for j in range(1, n):
            dp[0][j] = int(dp[0][j-1] == 1 and obstacleGrid[0][j] == 0)

        # Fill in the rest of the DP table
        for i in range(1, m):
            for j in range(1, n):
                # If there is no obstacle, the number of ways to reach this cell
                # is the sum of ways to reach the cell above and the cell to the left
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # The value in the bottom-right cell is the number of unique paths to that cell
        return dp[m-1][n-1]

# Testcases
sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # Output: 2
print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))  # Output: 1


# Description:
'''
In this code:

-    We first check if the starting cell (top-left corner) is an obstacle or if the grid is empty. If so, 
     there are no possible paths, so we return 0.
-    We then initialize a DP table with the same dimensions as the grid. This table will store the number 
     of ways to reach each cell.
-    The first cell (top-left corner) is initialized to 1, as there's one way to start (if it's not an obstacle).
-    The first column and first row are then initialized. If a cell in these areas is blocked by an obstacle, all 
     subsequent cells in that row or column are set to 0, as they become unreachable.
-    We then iterate over the rest of the grid. For each cell, if it's not an obstacle, we calculate the number 
     of ways to reach that cell as the sum of the number of ways to reach the cell directly above and the cell 
     directly to the left.
-    Finally, we return the value in the bottom-right corner of the DP table, which represents the total number 
     of unique paths to that cell.

'''