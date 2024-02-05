// 62. Unique Paths.

// Topic: Math, Dynamic Programming, Combinatorics.


/*
### Task:
---
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

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

### Testcase:
---
3
7
3
2


### Code:
---
class Solution {
public:
    int uniquePaths(int m, int n) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1)); // Initialize all values to 1

        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]; // Sum of paths from top and left
            }
        }

        return dp[m - 1][n - 1]; // Return the number of paths to the bottom-right corner
    }
};

// Description: ===================================
/*
To solve the "Unique Paths" problem, we can use dynamic programming to calculate the number of unique paths to each cell in the grid, 
or we can use a combinatorial approach based on the observation that any path from the top-left corner to the bottom-right corner 
consists of exactly `m-1` moves down and `n-1` moves right, regardless of the order.

### Solution 1: Dynamic Programming Approach:

In the dynamic programming approach, we create a 2D array `dp` where `dp[i][j]` represents the number of unique paths to reach cell `(i, j)` from the top-left corner. The top row and the first column are initialized to `1` since there is only one way to reach any cell in the top row or the first column (all moves are either right or down). For other cells, the number of paths to reach `dp[i][j]` is the sum of paths to reach the cell directly above it (`dp[i-1][j]`) and the cell to the left of it (`dp[i][j-1]`).
^ Look code  ^


### Solution 2: Combinatorial Approach:

The combinatorial solution observes that to reach the bottom-right corner, the robot must make exactly `m-1` moves down and `n-1` moves right, in any order. Thus, the problem reduces to calculating the number of ways to arrange `m-1` downs among `m+n-2` moves, which is a classic combination problem `C(m+n-2, m-1)`.

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        // Use long long to avoid integer overflow
        long long ans = 1;
        int j = 1;
        // Calculate C(m+n-2, m-1) = (m+n-2)! / ((m-1)!*(n-1)!)
        for (int i = m; i < m + n - 1; i++, j++) {
            ans *= i;
            ans /= j;
        }
        return (int)ans;
    }
};
```

### Description:

- **Dynamic Programming Approach**: The `dp` array is filled iteratively, where each cell's value is computed based on the values of the cell above it and the cell to the left of it. This solution has a time complexity of O(m*n) and a space complexity of O(m*n).
  
- **Combinatorial Approach**: This approach calculates the binomial coefficient `C(m+n-2, m-1)` directly, which represents the number of ways to choose `m-1` movements down out of `m+n-2` total movements (the remaining will obviously be to the right). This approach has a time complexity of O(min(m, n)) since it iterates through the smaller dimension and a space complexity of O(1).

*/
