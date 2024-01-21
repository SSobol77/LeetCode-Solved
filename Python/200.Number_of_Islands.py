# 200. Number of Islands.

# Topic: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix.

"""
## Task:
---------
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

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

## Testcase:
-------------
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]


## Code:
----------
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
"""
# Solution

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = 0
        
        # Define a DFS function to explore land cells and mark them as visited
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
                return
            grid[row][col] = '0'  # Mark the current cell as visited
            
            # Explore all four directions: up, down, left, right
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        # Iterate through all cells in the grid
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    islands += 1  # Increment the island count
                    dfs(row, col)  # Start DFS from the current land cell
        
        return islands  # Return the total number of islands



# Description
'''
To solve this problem, you can use Depth-First Search (DFS) or Breadth-First Search (BFS) to traverse
the grid and count the number of islands.


This code defines a `numIslands` method that counts the number of islands in a given grid. 

Here's a breakdown of the comments:

1. Check if the grid is empty. If it is, return 0, as there are no islands.

2. Get the dimensions of the grid (m rows and n columns) and initialize the island count.

3. Define a DFS (Depth-First Search) function named `dfs` that explores land cells and marks them as visited by changing '1' to '0'.

4. Iterate through all cells in the grid using nested loops.

5. If a cell contains '1', increment the island count and start DFS from that cell to explore the connected land cells.

6. Finally, return the total number of islands found.

'''
