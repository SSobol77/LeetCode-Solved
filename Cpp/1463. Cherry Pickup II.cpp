// 1463. Cherry Pickup II.      -HARD-


// Topic: Array, Dynamic Programming, Matrix.


/*
### Task:
---
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

    - Robot #1 is located at the top-left corner (0, 0), and
    - Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

    - From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
    - When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
    - When both robots stay in the same cell, only one takes the cherries.
    - Both robots cannot move outside of the grid at any moment.
    - Both robots should reach the bottom row in grid.
    

Example 1:
Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

Example 2:
Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
 
Constraints:
rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100

Hint 1:
Use dynammic programming, define DP[i][j][k]: The maximum cherries that both robots can take starting on the ith row,
and column j and k of Robot 1 and 2 respectively.


### Testcase:
---
[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
[[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]


### Code:
---
class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        
    }
};


*/
// Solution: --------------------------------------

class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        // Initialize the DP table with -1, indicating unvisited states
        vector<vector<vector<int>>> dp(rows, vector<vector<int>>(cols, vector<int>(cols, -1)));

        // Helper function to calculate the maximum cherries collected
        function<int(int, int, int)> dfs = [&](int row, int col1, int col2) -> int {
            // Base case: if out of bounds, return 0
            if (col1 < 0 || col1 >= cols || col2 < 0 || col2 >= cols) return 0;
            // If the state has been visited, return the stored value
            if (dp[row][col1][col2] != -1) return dp[row][col1][col2];
            // Current cherries picked by both robots
            int result = grid[row][col1];
            if (col1 != col2) result += grid[row][col2]; // Add cherries from second robot if not in the same cell

            // If not at the last row, explore further
            if (row < rows - 1) {
                int maxCherries = 0;
                // Consider all possible moves for both robots
                for (int newCol1 = col1 - 1; newCol1 <= col1 + 1; ++newCol1) {
                    for (int newCol2 = col2 - 1; newCol2 <= col2 + 1; ++newCol2) {
                        maxCherries = max(maxCherries, dfs(row + 1, newCol1, newCol2));
                    }
                }
                result += maxCherries; // Add the maximum cherries collected from deeper levels
            }

            dp[row][col1][col2] = result; // Store the result in the DP table
            return result;
        };

        // Start the DFS from the top row with robots at the corners
        return dfs(0, 0, cols - 1);
    }
};


// Description: ===================================
/*
To solve the Cherry Pickup II problem using dynamic programming, we will implement a function `cherryPickup` that takes a matrix `grid` as input and returns the maximum number of cherries that both robots can collect. We will use a 3-dimensional dynamic programming (DP) table to keep track of the maximum cherries collected so far for any given position of the two robots at a certain row.

The DP state will be `dp[row][col1][col2]`, representing the maximum number of cherries collected when robot #1 is at `(row, col1)` and robot #2 is at `(row, col2)`. The transition will involve considering all possible moves of both robots from the current state and maximizing the cherries collected based on these moves.

In this solution, we use a top-down approach with memoization. The `dfs` function is a recursive function that calculates the maximum number of cherries that can be picked up from the current row to the bottom of the grid for given positions of the two robots. We explore all possible moves of both robots from their current positions and use memoization to avoid recalculating states that have already been computed. This approach ensures that each state is computed only once, leading to an efficient solution.

*/
