// 994. Rotting Oranges.


// Topic: Array, Breadth-First Search, Matrix.


/*
### Task:
---
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

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


### Testcase:
---
[[2,1,1],[1,1,0],[0,1,1]]
[[2,1,1],[0,1,1],[1,0,1]]
[[0,2]]


### Code:
---
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        
    }
};


*/
// Solution: --------------------------------------

#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int, int>> q; // Queue to store the positions of rotten oranges
        int freshOranges = 0; // Count of fresh oranges

        // Initialize the queue with all rotten oranges and count fresh oranges
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    freshOranges++;
                }
            }
        }

        // Directions array for 4-directional movement
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int minutes = 0; // Minutes elapsed

        // BFS from all rotten oranges
        while (!q.empty() && freshOranges > 0) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto [x, y] = q.front();
                q.pop();
                // Explore all 4 directions
                for (auto [dx, dy] : directions) {
                    int newX = x + dx, newY = y + dy;
                    // Check if the new position is valid and has a fresh orange
                    if (newX >= 0 && newX < rows && newY >= 0 && newY < cols && grid[newX][newY] == 1) {
                        grid[newX][newY] = 2; // Make the orange rotten
                        q.push({newX, newY}); // Add it to the queue
                        freshOranges--; // Decrease the count of fresh oranges
                    }
                }
            }
            minutes++; // Increase the time after each level of BFS
        }

        // If there are still fresh oranges left, return -1
        return freshOranges == 0 ? minutes : -1;
    }
};


// Description: ===================================
/*
To solve the "Rotting Oranges" problem, we can use a Breadth-First Search (BFS) approach. The idea is to start the BFS from all the rotten oranges at the same time, and in each step, make all the adjacent fresh oranges rotten. We keep track of the time taken to rot each orange, and the maximum time taken in the process will be the answer. If there are still fresh oranges left at the end, we return -1, indicating it's impossible to rot all oranges.

### Description:

- **Initialization**: We start by counting all the fresh oranges and adding all the rotten oranges to a queue.
- **BFS**: We perform a BFS starting from all the rotten oranges simultaneously. In each step of the BFS, we rot all the adjacent fresh oranges.
- **Time Tracking**: We keep track of the time by incrementing a `minutes` counter after each level of BFS is completed.
- **Fresh Oranges Check**: If there are fresh oranges left after the BFS, we return -1, indicating it's impossible to rot all oranges. Otherwise, we return the `minutes` counter, which represents the minimum time required to rot all oranges.

*/
