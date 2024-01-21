# 200. Number of Islands

# Topic: Array, Depth-First Search. Breadth-First Search, Union Find, Matrix.

'''
# Task:
-------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume 
all four edges of the grid are all surrounded by water. 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.


# Testcase
----------
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]


# Code:
--------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
  


'''
# Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            # Check if the current cell is within the grid and is part of an island
            if 0 <= row < m and 0 <= col < n and grid[row][col] == '1':
                # Mark the cell as visited ('2') and recursively explore neighboring cells
                grid[row][col] = '2'
                dfs(row - 1, col)  # Up
                dfs(row + 1, col)  # Down
                dfs(row, col - 1)  # Left
                dfs(row, col + 1)  # Right
        
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        num_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands


# Test case 1
grid1 = [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]
output1 = Solution().numIslands(grid1)  # Should return 1

# Test case 2
grid2 = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]
output2 = Solution().numIslands(grid2)  # Should return 3

# Print test results
print(output1)  # 1
print(output2)  # 3


# Description:
'''
This code defines a class Solution that provides a method numIslands for counting the number of islands in a 2D binary grid.
The algorithm uses Depth-First Search (DFS) to traverse the grid and identify connected cells that form an island.
For each cell with a value of '1' (land), it marks the cell as visited ('2') and explores neighboring cells recursively.
The algorithm counts the number of times it starts DFS from a '1', which represents the number of islands in the grid.

'''
