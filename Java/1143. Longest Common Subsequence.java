// 1143. Longest Common Subsequence

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
    public int longestCommonSubsequence(String text1, String text2) {
        
    }
}

*/
// Solution: --------------------------------------

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        // m and n store the lengths of the first and second string, respectively.
        int m = text1.length();
        int n = text2.length();
        
        // dp array to store the length of the longest common subsequence at each point.
        // dp[i][j] represents the LCS length for text1[0...i-1] and text2[0...j-1].
        int[][] dp = new int[m + 1][n + 1];

        // Iterate through each character of both strings.
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If characters match, the LCS is 1 plus the LCS of the previous characters.
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    // If characters don't match, take the maximum LCS by either skipping a character
                    // from text1 or text2, thus exploring both possibilities.
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        // The bottom-right cell contains the length of the LCS for the entire strings.
        return dp[m][n];
    }
}


// Description:
/*
To solve the "Longest Common Subsequence" problem using dynamic programming, you can follow the hints provided. 
The idea is to create a 2D array `dp` where `dp[i][j]` represents the length of the longest common subsequence between 
the substrings `text1[0...i-1]` and `text2[0...j-1]`. 

Here's how you can approach it:

1. Initialize a 2D array `dp` with dimensions `[text1.length() + 1][text2.length() + 1]`. The extra row and column are used to 
   handle the base case where one of the strings is empty.

2. Iterate over each character in `text1` and `text2`. For each pair of characters:
   - If the characters are the same, the longest common subsequence up to those characters is 1 plus the longest common subsequence 
     up to the previous characters in each string. This is because the current characters can be added to the previous longest common 
     subsequence.
   - If the characters are different, the longest common subsequence up to those characters is the maximum of either ignoring the 
     current character of `text1` or `text2`.

3. The value in `dp[text1.length()][text2.length()]` will be the length of the longest common subsequence of `text1` and `text2`.

This code systematically builds up the solution for longer and longer subsequences by considering one character at a time from each 
string. By the end of the iteration, `dp[m][n]` holds the length of the longest common subsequence.

*/
