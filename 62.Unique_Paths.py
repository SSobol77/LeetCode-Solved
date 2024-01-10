# 62. Unique Paths.

# Topic: Math, Dynamic Programming, Combinatorics.

"""
## Task:
---------
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either 
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the 
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100


## Testcase:
-------------
3
7
3
2


## Code:
----------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

"""
# Solution 1,2:

## 1. The combinatorics approach:

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        # Import the factorial function from the math module
        from math import factorial

        # Calculate the total number of moves needed: 
        # (m-1) moves down and (n-1) moves right, total of (m+n-2) moves
        total_moves = m + n - 2

        # Calculate the number of moves in one direction (either down or right)
        # We choose the smaller number for efficiency
        moves_in_one_direction = min(m - 1, n - 1)

        # Calculate the number of unique paths using the formula for combinations:
        # C(total_moves, moves_in_one_direction) = total_moves! / (moves_in_one_direction! * (total_moves - moves_in_one_direction)!)
        return factorial(total_moves) // (factorial(moves_in_one_direction) * factorial(total_moves - moves_in_one_direction))


## 2. The dynamic programming approach:

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D list (matrix) with 1s. Each cell represents the number of paths to that cell.
        dp = [[1]*n for _ in range(m)]

        # Iterate through the matrix, starting from row 1 and column 1
        # (since the first row and first column are already initialized to 1s)
        for i in range(1, m):
            for j in range(1, n):
                # The value in each cell is the sum of the values from the cell above and the cell to the left.
                # This is because the robot can only come from the top (above) or from the left.
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # The bottom-right corner of the matrix will hold the total number of unique paths
        return dp[m-1][n-1]


# Description
'''
The problem of finding the number of unique paths for a robot on an m x n grid can be approached using dynamic programming 
or combinatorics. The robot starts at the top-left corner and can only move right or down, aiming to reach the bottom-right 
corner. The task is to calculate the total number of distinct paths possible.

### Dynamic Programming Approach:
---------------------------------
1. **Initialization**: Create a 2D array `dp` of size m x n. `dp[i][j]` will store the number of ways to reach the cell `(i, j)`.

2. **Base Case**: Since there's only one way to move along the top row or the left column (either right or down respectively),
     set all values in the first row and first column of `dp` to 1.

3. **Fill the DP Table**: 
   - Iterate over the grid starting from `dp[1][1]`.
   - For each cell `(i, j)`, the number of ways to reach it is the sum of ways to reach the cell above it (`dp[i-1][j]`) and 
     the cell to its left (`dp[i][j-1]`).
   - Formula: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`.

4. **Result**: The bottom-right corner `dp[m-1][n-1]` will hold the total number of unique paths.

### Combinatorics Approach:
---------------------------
Another way to solve this problem is by using combinatorics. The robot has to make exactly `m-1` moves down and `n-1` moves 
right, irrespective of the order. So, the problem reduces to calculating the number of ways to choose `m-1` moves from `m+n-2` 
total moves (or equivalently, choosing `n-1` right moves from `m+n-2` moves).

- **Formula**: The number of unique paths is given by the binomial coefficient: C(m+n-2, m-1) or C(m+n-2, n-1). This can be 
    calculated using the formula for combinations.


### Python Implementation:

Here's how the combinatorics approach can be implemented in Python:
-------------------------------------------------------------------
```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from math import factorial
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))
```

And here's the dynamic programming approach:
-----------------------------------------------
```
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
```

### Test Cases:
To test these solutions, you can use the provided test cases like `(m=3, n=7)` which should return `28`, and `(m=3, n=2)` 
which should return `3`.

Both methods are efficient, but the combinatorics approach is more concise and avoids the need for extra space required 
by the dynamic programming approach.

'''