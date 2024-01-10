# 72. Edit Distance.

# Topic: String, Dynamic Programming.


'''
# Task:
-----------
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

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


# Testcase
-----------
"horse"
"ros"
"intention"
"execution"

# Code
-----------
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
 
'''
# Solution:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Initialize the DP table with dimensions (m+1) x (n+1)
        # +1 to include the case of empty string (base case)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases:
        # Filling the first column: converting word1 to an empty string requires i deletions
        for i in range(m + 1):
            dp[i][0] = i
        # Filling the first row: converting an empty string to word2 requires j insertions
        for j in range(n + 1):
            dp[0][j] = j

        # Build the DP table iteratively
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If the characters match, no operation needed, carry over the previous count
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # If characters don't match, consider all three operations
                    # and take the minimum
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # Delete a character from word1
                        dp[i][j - 1],    # Insert a character into word1
                        dp[i - 1][j - 1]  # Replace a character in word1
                    )

        # The value at dp[m][n] is the minimum number of operations needed
        # to convert word1 into word2
        return dp[m][n]

# Testcases
sol = Solution()
print(sol.minDistance("horse", "ros"))          # Output: 3
print(sol.minDistance("intention", "execution"))  # Output: 5


# Description:
'''
In this code:

-We initialize a 2D array dp where dp[i][j] represents the minimum number of operations required to convert the first 
 i characters of word1 to the first j characters of word2.
-The first row and the first column of the dp array are initialized with their index values. This is because converting
 a non-empty string to an empty string (or vice versa) requires a number of operations equal to the length of the string
 (either all deletions or all insertions).
-For each pair of indices (i, j), we check if the characters in word1 and word2 at those indices are the same. If they 
 are, no additional operation is required, and we carry over the number of operations from dp[i-1][j-1].
-If the characters are different, we consider the minimum number of operations among deleting a character from word1, 
 inserting a character into word1, or replacing a character in word1. We add 1 to this minimum number since we're performing
 one operation.
-The final answer is found at dp[m][n], which gives the minimum number of operations required to convert word1 to word2.

'''
