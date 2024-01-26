// 51. N-Queens.           - HARD -

// Topic: Array, Backtracking.

/*
### Task:
---
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens 
attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in 
any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both 
indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9


# Testcase:
---
4
1


# Code:
---
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        
    }
};

*/
// Solution:  --------------------------------------------------------------------------------

#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> solutions; // Stores all possible solutions
        vector<string> board(n, string(n, '.')); // Initialize the board with all empty spaces

        // Flags for checking the availability of columns and diagonals
        vector<int> flags_col(n, 1), flags_45(2 * n - 1, 1), flags_135(2 * n - 1, 1); 

        // Start the backtracking process from the first row
        backtrack(solutions, board, flags_col, flags_45, flags_135, 0, n);
        return solutions;
    }

private:
    // Recursive function to place queens and explore solutions
    void backtrack(vector<vector<string>>& solutions, vector<string>& board, vector<int>& flags_col, vector<int>& flags_45, vector<int>& flags_135, int row, int n) {
        if (row == n) {
            // A valid solution is found when all queens are placed
            solutions.push_back(board);
            return;
        }

        // Try placing a queen in each column of the current row
        for (int col = 0; col < n; ++col) {
            // Check if the current cell is safe for placing a queen
            if (isSafe(flags_col, flags_45, flags_135, row, col, n)) {
                board[row][col] = 'Q'; // Place the queen
                // Update the flags to indicate the column and diagonals are no longer available
                updateFlags(flags_col, flags_45, flags_135, row, col, n, 0);

                // Move to the next row
                backtrack(solutions, board, flags_col, flags_45, flags_135, row + 1, n);

                // Backtrack: Remove the queen and restore flags
                board[row][col] = '.';
                updateFlags(flags_col, flags_45, flags_135, row, col, n, 1);
            }
        }
    }

    // Function to check if a cell is safe for placing a queen
    bool isSafe(vector<int>& flags_col, vector<int>& flags_45, vector<int>& flags_135, int row, int col, int n) {
        // A cell is safe if no other queen is present in the same column, 45-degree and 135-degree diagonals
        return flags_col[col] && flags_45[row + col] && flags_135[n - 1 + col - row];
    }

    // Function to update flags when placing or removing a queen
    void updateFlags(vector<int>& flags_col, vector<int>& flags_45, vector<int>& flags_135, int row, int col, int n, int isPut) {
        // Set or reset the flags for the column and diagonals
        flags_col[col] = isPut;
        flags_45[row + col] = isPut;
        flags_135[n - 1 + col - row] = isPut;
    }
};


// Description:  =============================================================================
/*

The N-Queens problem is a classic example of a backtracking problem. The goal is to place N queens on an N×N chessboard 
such that no two queens threaten each other. This implies that no two queens can be placed in the same row, column, or diagonal.

To solve this, we can use a depth-first search approach, where we try to place a queen in each row and use backtracking to 
explore all possible placements in subsequent rows. If at any point a placement leads to a conflict, we backtrack and try a 
different placement.


### Explanation:

1. **Initializing the Board and Flags**: We start by initializing the chessboard and setting up flags for each column and the 
   two diagonals. A flag value of `1` indicates that the corresponding column or diagonal is free.

2. **Backtracking Function**: The `backtrack` function tries to place a queen in each column of the current row and then 
   recursively calls itself for the next row.

3. **Checking Safety**: The `isSafe` function checks if a cell is safe to place a queen. It ensures that no other queen is 
   placed in the same column, 45-degree diagonal, or 135-degree diagonal.

4. **Updating Flags**: The `updateFlags` function updates the flags when placing or removing a queen. When a queen is placed, 
   the corresponding column and diagonal flags are set to `0` (not free), and when a queen is removed (backtracking), they are 
   reset to `1` (free).

5. **Valid Solution**: Once all rows have been processed (i.e., `row == n`), a valid configuration of the board is added to 
   the solutions.

6. **Placing and Removing Queens**: The algorithm tries placing a queen in each column of the current row. If a placement is 
   safe, it proceeds to the next row. If no safe placement is found in a row, it backtracks and tries a different placement in 
   the previous row.

This solution effectively generates all possible solutions for the N-Queens problem using backtracking, ensuring that no two 
queens threaten each other.

*/