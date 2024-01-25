//1143. Longest Common Subsequence

// Topic: String, Dynamic Programming.


/*
### Task:
---
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing 
the relative order of the remaining characters.

  * For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

Hint 1:
Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
Hint 2:
DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise


### Testcase:
---
"abcde"
"ace"
"abc"
"abc"
"abc"
"def"


### Code:
---
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        
    }
};

*/
// Solution: --------------------------------------

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        // Get the lengths of the two strings
        int m = text1.size();
        int n = text2.size();

        // Initialize a 2D vector 'dp' with dimensions (m+1) x (n+1)
        // The additional row and column are for the base case where one string is empty
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // Iterate over each character of 'text1' and 'text2'
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                // If the current characters of 'text1' and 'text2' match
                if (text1[i - 1] == text2[j - 1]) {
                    // Include this character in the LCS count, add 1 to the count of the previous subsequence
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    // If the characters do not match, the current LCS count is the max of the LCS excluding
                    // the current character from either 'text1' or 'text2'
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        // The element dp[m][n] holds the length of the longest common subsequence of 'text1' and 'text2'
        return dp[m][n];
    }
};



// Description: ===================================
/*
To solve the problem of finding the longest common subsequence (LCS) between two strings, `text1` and `text2`, dynamic programming is an efficient 
approach. We will use a 2D array, `dp`, where `dp[i][j]` represents the length of the LCS between the first `i` characters of `text1` and the 
first `j` characters of `text2`. 

The algorithm works as follows:
1. Initialize a 2D array `dp` of size `(length of text1 + 1) x (length of text2 + 1)` with all elements set to 0.
2. Iterate over each character in `text1` and `text2`.
3. If a pair of characters from `text1` and `text2` match, the value in `dp[i][j]` is 1 plus the value of `dp[i-1][j-1]`.
4. If they don't match, `dp[i][j]` is the maximum of `dp[i-1][j]` and `dp[i][j-1]`.
5. The value in `dp[length of text1][length of text2]` will be the length of the LCS.

### Description
---
In the solution, the `dp` array is initialized with dimensions `(m+1) x (n+1)`, where `m` and `n` are the lengths of `text1` and `text2`, respectively. 
The extra row and column are used to handle the cases where a subsequence ends at the beginning of `text1` or `text2`. We then iterate through each 
character pair and apply the dynamic programming logic mentioned earlier. The final result, which is the length of the longest common subsequence, is 
stored in `dp[m][n]`.

### Commented Explanation
---
- The `dp` 2D vector is initialized with dimensions `(m+1) x (n+1)`. This includes an additional row and column to handle empty subsequences.
- The outer loop iterates over the characters of `text1`, and the inner loop iterates over the characters of `text2`.
- If the characters in the current positions of `text1` and `text2` match, the corresponding `dp` value is incremented by 1 from the value of the previous subsequence (diagonally up-left).
- If the characters do not match, the `dp` value is set to the maximum value between the left and top adjacent cells. This represents the longest subsequence found so far excluding the current character from either `text1` or `text2`.
- Finally, `dp[m][n]` gives the length of the LCS, which is the required output.

*/
