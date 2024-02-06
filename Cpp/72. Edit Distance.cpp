// 72. Edit Distance.


// Topic: String, Dynamic Programming.


/*
### Task:
---
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

  -  Insert a character
  -  Delete a character
  -  Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

### Testcase:
---
"horse"
"ros"
"intention"
"execution"


### Code:
---
class Solution {
public:
    int minDistance(string word1, string word2) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length(), n = word2.length();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        // Initialize the first row and column
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        // Fill in the dp table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    // Characters match, no operation required
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Consider all operations and find the minimum
                    dp[i][j] = 1 + min({
                        dp[i - 1][j],    // Deletion
                        dp[i][j - 1],    // Insertion
                        dp[i - 1][j - 1] // Replacement
                    });
                }
            }
        }

        // The bottom-right corner of dp contains the answer
        return dp[m][n];
    }
};



// Description: ===================================
/*
The "Edit Distance" problem, also known as the Levenshtein distance, measures the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into another. This problem can be solved efficiently using dynamic programming.

### Dynamic Programming Approach:
1. Create a 2D array `dp` with dimensions `(m+1) x (n+1)`, where `m` is the length of `word1` and `n` is the length of `word2`. `dp[i][j]` will represent the minimum edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`.
2. Initialize the first row and first column of `dp`. `dp[i][0]` is set to `i` because converting a string of length `i` to an empty string requires `i` deletions. Similarly, `dp[0][j]` is set to `j`, representing `j` insertions to convert an empty string to a string of length `j`.
3. Iterate over each cell in `dp`, filling in each cell using the following rules:
   - If `word1[i-1] == word2[j-1]`, set `dp[i][j] = dp[i-1][j-1]` as no operation is needed for the last character.
   - Otherwise, set `dp[i][j]` to the minimum of the three possible operations (insert, delete, replace) plus 1. Mathematically, `dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])`.
4. The value at `dp[m][n]` will be the minimum edit distance between `word1` and `word2`.


### Description:
- **Lines 6-8:** Initialize the first column of the DP table. Each cell `dp[i][0]` is set to `i`, representing `i` deletions to convert `word1` substring of length `i` to an empty string.
- **Lines 9-11:** Initialize the first row of the DP table. Each cell `dp[0][j]` is set to `j`, representing `j` insertions to convert an empty string to `word2` substring of length `j`.
- **Lines 13-22:** Fill in the DP table. If the current characters in `word1` and `word2` match, no additional edit is needed for this step (`dp[i][j] = dp[i-1][j-1]`). If they don't match, we consider the minimum cost among deleting a character from `word1`, inserting a character into `word1`, and replacing a character in `word1`, and add 1 to that minimum cost.
- **Line 25:** The value in `dp[m][n]` gives the minimum number of operations required to convert `word1` into `word2`.



*/