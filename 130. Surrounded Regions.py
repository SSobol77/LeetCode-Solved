# 130. Surrounded Regions

# Topic: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix.

''''
# Task:
-------
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
 

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]
 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.


# Testcase:
-----------
[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
[["X"]]

# Code:
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

'''
# Solution
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        m, n = len(board), len(board[0])

        def dfs(row, col):
            # Check if the current cell is within the grid and is 'O'
            if 0 <= row < m and 0 <= col < n and board[row][col] == 'O':
                # Mark the cell as 'E' to indicate it's part of the region
                board[row][col] = 'E'
                # Recursively explore neighboring cells
                dfs(row - 1, col)  # Up
                dfs(row + 1, col)  # Down
                dfs(row, col - 1)  # Left
                dfs(row, col + 1)  # Right
        
        # Traverse the border and mark all connected 'O' cells as 'E'
        for i in range(m):
            dfs(i, 0)  # Left border
            dfs(i, n - 1)  # Right border
        for j in range(n):
            dfs(0, j)  # Top border
            dfs(m - 1, j)  # Bottom border
        
        # Update the board: 'E' becomes 'O' and 'O' becomes 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'E':
                    board[i][j] = 'O'


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    board1 = [
      ["X", "X", "X", "X"],
      ["X", "O", "O", "X"],
      ["X", "X", "O", "X"],
      ["X", "O", "X", "X"]
    ]
    solution.solve(board1)
    print(board1)
    
    # Test case 2
    board2 = [["X"]]
    solution.solve(board2)
    print(board2)
    
    # Test case 3
    board3 = [
      ["X", "O", "X", "X"],
      ["X", "O", "O", "X"],
      ["X", "X", "O", "X"],
      ["X", "O", "X", "X"]
    ]
    solution.solve(board3)
    print(board3)


# Descripton:
'''
You are given an m x n matrix board containing 'X' and 'O'. The goal is to capture all regions that 
are 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that 
surrounded region.

A region is considered surrounded by 'X' if all 'O's in the region are either on the border of the
matrix or are connected to other 'O's on the border.

Write a function solve(board: List[List[str]]) that modifies the board in-place to capture the 
surrounded regions.

'''
