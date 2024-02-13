//200. Number of Islands.


// Topic: Array, Depth-First Search, Breadth-First Search, Union Find, Matrix.


/*
### Task:
---
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


### Testcase:
---
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]


### Code:
---
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
    }
};

*/
// Solution: --------------------------------------

#include <vector>
using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        // Check if the grid is empty
        if (grid.empty()) return 0;

        int num_islands = 0; // Initialize island count
        int rows = grid.size(); // Number of rows in the grid
        int cols = grid[0].size(); // Number of columns in the grid

        // Iterate through each cell in the grid
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                // If the cell is land ('1'), perform DFS to mark all connected lands
                if (grid[i][j] == '1') {
                    dfs(grid, i, j); // Perform DFS to mark the island
                    ++num_islands; // Increment island count after marking all parts of the island
                }
            }
        }

        return num_islands; // Return the total number of islands found
    }

private:
    void dfs(vector<vector<char>>& grid, int i, int j) {
        int rows = grid.size(); // Number of rows in the grid
        int cols = grid[0].size(); // Number of columns in the grid

        // Base case: Check for invalid indices or if the current cell is water ('0')
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] == '0') {
            return; // Stop DFS if out of bounds or at a water cell
        }

        // Mark the current cell as visited by setting it to '0'
        grid[i][j] = '0';

        // Recursively explore all neighboring cells (vertically and horizontally)
        dfs(grid, i - 1, j); // Explore upwards
        dfs(grid, i + 1, j); // Explore downwards
        dfs(grid, i, j - 1); // Explore leftwards
        dfs(grid, i, j + 1); // Explore rightwards
    }
};




// Description: ===================================
/*
To solve the "Number of Islands" problem, we can use Depth-First Search (DFS) to explore each island and mark the visited parts to avoid counting them more than once. When we find a land cell ('1'), we perform a DFS from that cell, marking all connected land cells as visited, effectively sinking the island. We then continue scanning the grid for the next unvisited land cell, which will be the start of a new island. Each time we start a new DFS, we increment our island count.

### Description:

- The `numIslands` function iterates through each cell in the grid.
- When it finds a land cell ('1'), it calls the `dfs` function to perform a depth-first search from that cell.
- The `dfs` function marks the current cell as visited (by setting it to '0') and then recursively explores the neighboring cells (up, down, left, right) that are also land cells.
- Each call to `dfs` from `numIslands` represents the discovery of a new island, so we increment the `num_islands` count.
- The process continues until all cells in the grid have been visited, and the total number of islands is returned.



*/