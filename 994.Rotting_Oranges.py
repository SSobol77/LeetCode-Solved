# 994. Rotting Oranges.

# Topic: Array, Breadth-First Search, Matrix.

"""
## Task:
---------
You are given an m x n grid where each cell can have one of three values:

 - 0 representing an empty cell,
 - 1 representing a fresh orange, or
 - 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.


## Testcase:
-------------
[[2,1,1],[1,1,0],[0,1,1]]
[[2,1,1],[0,1,1],[1,0,1]]
[[0,2]]


## Code:
----------
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

"""
# Solution

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        rotten_oranges = deque()
        
        # Count the fresh oranges and locate the rotten ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges.append((i, j, 0))  # (row, col, minutes)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4 possible directions to adjacent cells
        minutes = 0  # Initialize the minutes counter
        
        while rotten_oranges:
            i, j, minutes = rotten_oranges.popleft()  # Get the position and minutes of the rotten orange
            
            for dx, dy in directions:
                ni, nj = i + dx, j + dy  # Calculate the new position
                
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    # If the new position is within the grid and has a fresh orange
                    grid[ni][nj] = 2  # Mark it as rotten
                    fresh_oranges -= 1  # Decrease the count of fresh oranges
                    rotten_oranges.append((ni, nj, minutes + 1))  # Add it to the queue with updated minutes
        
        # After the BFS traversal, check if there are any remaining fresh oranges
        # If there are, it means not all oranges can be rotten, so return -1
        # Otherwise, return the number of minutes it took to rot all oranges
        return minutes if fresh_oranges == 0 else -1


### Description
'''
To solve this problem, you can use a Breadth-First Search (BFS) algorithm to simulate the rotting process of oranges in the grid.

This orangesRotting method used of the Solution class to find the minimum number of minutes needed to rot all oranges in the grid. 
The BFS algorithm is used to simulate the rotting process, and the function returns the required minutes or -1 if it's impossible 
to rot all the fresh oranges.

'''
