# 576. Out of Boundary Paths.

# Topic: Dynamic Programming

"""
### Task:
---
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball 
to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary.
Since the answer can be very large, return it modulo 109 + 7.

 
Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n

Hint 1:
Is traversing every path feasible? There are many possible paths for a small matrix. Try to optimize it.
Hint 2:
Can we use some space to store the number of paths and update them after every move?
Hint 3:
One obvious thing: the ball will go out of the boundary only by crossing it. Also, there is only one possible 
way the ball can go out of the boundary from the boundary cell except for corner cells. From the corner cell,
the ball can go out in two different ways. Can you use this thing to solve the problem?

### Testcase:
---
2
2
2
0
0
1
3
3
0
1


### Code:
---
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        

"""
### Solution: --------------------------------------

from functools import cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Calculate the number of ways to move a ball out of a grid boundary within a maximum number of moves.

        Args:
        m (int): Number of rows in the grid.
        n (int): Number of columns in the grid.
        maxMove (int): Maximum number of moves allowed.
        startRow (int): Starting row position of the ball.
        startColumn (int): Starting column position of the ball.

        Returns:
        int: The number of paths to move the ball out of the grid boundary.
        """
        # Define a large prime number for modulo operation to avoid integer overflow
        MOD = 10**9 + 7

        @cache
        def countPaths(row: int, col: int, moves: int) -> int:
            """
            Helper function to recursively count the paths from a given position with remaining moves.

            This function uses memoization (caching) to store results of subproblems to avoid redundant calculations.

            Args:
            row (int): Current row position of the ball.
            col (int): Current column position of the ball.
            moves (int): Remaining moves.

            Returns:
            int: Number of paths from the current position to outside the grid.
            """
            # If the position is out of grid boundaries, it's a valid path
            if row < 0 or row == m or col < 0 or col == n:
                return 1
            # If no moves left, no path is possible
            if moves == 0:
                return 0

            # Recursive calls for all four directions (up, down, left, right)
            # The results are summed up to get the total number of paths from this position
            paths = (countPaths(row - 1, col, moves - 1) +
                     countPaths(row + 1, col, moves - 1) +
                     countPaths(row, col - 1, moves - 1) +
                     countPaths(row, col + 1, moves - 1)) % MOD

            return paths

        # Calculate the result starting from the initial position
        result = countPaths(startRow, startColumn, maxMove)

        # Clear the cache to free up memory after computation
        countPaths.cache_clear()

        return result

# Example usage
solution = Solution()
print(solution.findPaths(2, 2, 2, 0, 0))  # Output: 6
print(solution.findPaths(1, 3, 3, 0, 1))  # Output: 12


### Description: ===================================
'''
### Algorithm Description:

1. **Initialization:** The function `findPaths` is initialized with the grid dimensions (`m` and `n`), the maximum number of moves allowed (`maxMove`), 
   and the starting position of the ball (`startRow` and `startColumn`).

2. **Memoization Setup:** The `@cache` decorator from `functools` is used on the helper function `countPaths`. This function is responsible for 
   calculating the number of paths from a given position with a certain number of moves left. Memoization helps avoid recalculating paths for the same 
   position and number of moves.

3. **Recursive Path Counting:** The `countPaths` function uses recursion to explore all possible moves (up, down, left, right) from the current position. 
   If the position is out of the grid, it counts as a valid path. If there are no moves left, it returns 0, indicating no path.

4. **Modulo Operation:** To prevent integer overflow and keep the numbers within a manageable range, the total paths are calculated using a modulo 
   operation with a large prime number (`10**9 + 7`).

5. **Result Calculation and Cache Clearance:** The total number of paths is calculated by calling `countPaths` with the initial position and number 
   of moves. After the calculation, the cache is cleared to free up memory.

6. **Output:** The function returns the total number of paths from the starting position to outside the grid within the given number of moves. 

This algorithm efficiently calculates the number of paths using dynamic programming principles and memoization, making it suitable for large grids 
and a high number of moves.

'''
