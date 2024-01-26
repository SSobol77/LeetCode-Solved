// 79. Word Search.

// Topic: Array, Backtracking, Matrix.

/*
### Task:
---
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?


# Testcase:
---
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCCED"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"SEE"
[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
"ABCB"


# Code:
---
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        
    }
};
*/
// Solution: ---------------------------------------------------------------------------------

class Solution {
public:
    // DFS function to search the word starting from cell (x, y) in the grid.
    // wordIndex is the current position in the word that needs to be matched.
    bool dfs(vector<vector<char>>& board, string& word, int wordIndex, int x, int y) {
        // If wordIndex reaches the length of the word, the entire word is found.
        if (wordIndex == word.size()) return true;

        // Boundary check for the grid and character match check.
        if (x < 0 || y < 0 || x >= board.size() || y >= board[0].size() || board[x][y] != word[wordIndex]) {
            return false;
        }

        char temp = board[x][y];
        board[x][y] = '*'; // Mark the current cell as visited.

        // Explore all four directions: down, up, right, left.
        // If any direction returns true, the word is found.
        if (dfs(board, word, wordIndex + 1, x + 1, y) ||
            dfs(board, word, wordIndex + 1, x - 1, y) ||
            dfs(board, word, wordIndex + 1, x, y + 1) ||
            dfs(board, word, wordIndex + 1, x, y - 1)) {
            return true;
        }

        board[x][y] = temp; // Unmark the current cell (backtrack).
        return false;
    }

    // Main function to check if a word exists in the grid.
    bool exist(vector<vector<char>>& board, string word) {
        // Iterate over each cell of the grid.
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                // Start DFS from the current cell if the first character matches.
                if (dfs(board, word, 0, i, j)) {
                    return true; // If DFS finds the word, return true.
                }
            }
        }
        return false; // Word not found in the grid.
    }
};




// Description: ======================================================================================================
/*

To solve the "Word Search" problem, we need to implement a depth-first search (DFS) combined with backtracking. The idea is to 
search each cell in the grid and, if the first letter of the word matches the cell, proceed to check its neighbors (up, down, 
left, right) recursively for the next letters of the word.


### Approach:
1. **Traverse the Grid**: Loop through each cell in the grid.
2. **DFS & Backtracking**: When a cell matches the first letter of the word, call the DFS function to check its neighbors. The 
     DFS function will return true if it finds the complete word.
3. **Mark Visited Cells**: To avoid using the same cell more than once, temporarily mark the cell as visited during the DFS.
4. **Boundary and Matching Check**: Ensure that the DFS search stays within the grid's bounds and that each cell matches the 
     corresponding letter in the word.
5. **Search Pruning**: Return early if the word is found, or if a search path is invalid.


### Explanation:
- The `dfs` function performs a depth-first search from the current cell. It checks if the current cell matches the current 
  character of the word, and if so, it recursively checks its neighboring cells.
- Marking cells with '*' and later restoring their original character is a backtracking step to ensure the same cell is not 
  used more than once in the search for a single word.
- The `exist` function initiates the DFS search from every cell in the grid until it finds the word or exhausts all possibilities.


### Complexity Analysis:
- **Time Complexity**: O(M*N*4^L), where M and N are the dimensions of the board and L is the length of the word. In the worst 
    case, we might have to explore all 4 directions for each character of the word.
- **Space Complexity**: O(L) due to the recursion stack, where L is the length of the word.

*/
