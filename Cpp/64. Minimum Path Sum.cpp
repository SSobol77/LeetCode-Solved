// 64. Minimum Path Sum.

// Topic:Array,Dynamic Programming,Matrix.

/*
### Task:
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum 
of all numbers along its path.

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


### Testcase:
[[1,3,1],[1,5,1],[4,2,1]]
[[1,2,3],[4,5,6]]

### Code:
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        
    }
};

*/
// Solution: -----------------------------------------------

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, grid[0][0]));

        // Initialize the first row and first column of the DP table
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }
        for (int j = 1; j < n; j++) {
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }

        // Compute the minimum path sum for each cell
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // For each cell, choose the minimum path sum from the top or left cell and add the current cell's value
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }

        // The bottom-right cell contains the minimum path sum
        return dp[m - 1][n - 1];
    }
};

// Description: ============================================
/*
To solve the "Minimum Path Sum" problem, we can use dynamic programming. The idea is to update each cell in the grid with the minimum sum to reach that cell from the top left corner. We only need to consider two directions for each cell: from the left (i, j-1) and from the top (i-1, j). The minimum path sum for a cell (i, j) is the value in (i, j) plus the minimum of the sums of the cells from which we can arrive at (i, j), which are (i-1, j) and (i, j-1).

Here's a step-by-step approach to implement this:

1. Create a 2D DP array of the same size as the input grid to store the minimum sum path to reach each cell.
2. Initialize the first cell (top-left corner) of the DP array with the first cell of the grid since that's where we start.
3. Iterate through the grid row by row, and within each row column by column, updating the DP array:
   - For each cell, calculate the minimum path sum to reach that cell by considering the minimum path sum to reach the cell directly above and to the left, then add the current cell's value.
   - For the first row and first column, we only have one choice: move right from the left cell or move down from the top cell, respectively.
4. The bottom-right corner of the DP array will contain the minimum path sum from the top-left corner to the bottom-right corner.

### Explanation:
- **Line 3-4:** We get the dimensions of the grid (`m` and `n`) and initialize the DP table with the value of the first cell of the grid.
- **Lines 7-10:** We fill in the first column of the DP table. Each cell in the first column can only be reached from the cell directly above, so we add the current cell's value to the sum of the path to the cell above.
- **Lines 11-14:** Similarly, we fill in the first row of the DP table. Each cell in the first row can only be reached from the cell directly to the left, so we add the current cell's value to the sum of the path to the cell to the left.
- **Lines 17-21:** We iterate over the rest of the grid, computing the minimum path sum for each cell as the minimum of the sums of the top and left cells plus the current cell's value.
- **Line 24:** The minimum path sum to reach the bottom-right corner of the grid is contained in the bottom-right cell of the DP table, which we return as the solution.

*/
