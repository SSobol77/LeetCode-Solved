// 10. Regular Expression Matching

/*
### Task:
----
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

#Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

E#xample 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

#Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

#Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

### Code:
--------
class Solution {
public:
    bool isMatch(string s, string p) {
        
    }
};
*/

// Solution:
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        
        // Create a 2D DP table to store matching information
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Empty pattern matches empty string
        dp[0][0] = true;
        
        // Initialize the first row of DP table
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                // '*' can match zero preceding element
                dp[0][j] = dp[0][j - 2];
            }
        }
        
        // Fill in the DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                    // If current characters match or pattern is '.', inherit the match from the previous characters
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    // If current pattern character is '*', handle zero or more matches
                    dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'));
                }
            }
        }
        
        // The result is stored in dp[m][n], where m and n are the lengths of s and p
        return dp[m][n];
    }
};

// Description:
/*
This code uses a dynamic programming approach to check if the string s matches the pattern p. The dp table stores 
whether substrings of s and p up to certain lengths match. It iterates through both strings and updates the dp table
based on the current characters and patterns, taking into account '.' and '*'.

The final result is stored in dp[m][n], where m and n are the lengths of s and p, respectively. If dp[m][n] is true, 
it means the entire s matches the pattern p.

*/
