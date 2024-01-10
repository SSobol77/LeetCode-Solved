# 97. Interleaving String.

# Topic: String, Dynamic Programming.


'''
# Task:
-----------
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m
substrings
respectively, such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?




# Testcase:
------------
"aabcc"
"dbbca"
"aadbbcbcac"
"aabcc"
"dbbca"
"aadbbbaccc"
""
""
""


# Code:
------------
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
      
'''
# Solution:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if the combined length of s1 and s2 equals the length of s3
        if len(s3) != len(s1) + len(s2):
            return False

        # Initialize a 1D DP array with False, with an extra space for the empty string
        dp = [False] * (len(s2) + 1)

        # Iterate over both strings s1 and s2
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                # If both i and j are zero, it's an empty string case which is always True
                if i == 0 and j == 0:
                    dp[j] = True
                # If i is zero, compare characters of s2 and s3
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                # If j is zero, compare characters of s1 and s3
                elif j == 0:
                    dp[j] = dp[j] and s1[i-1] == s3[i+j-1]
                # For other cases, check if the current characters in s1 or s2 match with s3
                # and update the DP array accordingly
                else:
                    dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])

        # The last element of DP array tells if s3 can be formed by interleaving s1 and s2
        return dp[len(s2)]

# Testcases
sol = Solution()
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # Output: True
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # Output: False
print(sol.isInterleave("", "", ""))                      # Output: True


# Description:
'''
In this code:

-We first handle a base case where the lengths of s1, s2, and s3 are compared. If the length of s3 is not equal 
 to the sum of lengths of s1 and s2, it's impossible for s3 to be an interleaving of s1 and s2, so we return False.
-We use a dynamic programming approach where dp[j] stores whether the first i characters of s1 and the first j 
 characters of s2 can form the first i+j characters of s3.
-We iterate through each character in s1 and s2, updating the DP array based on whether the characters at the 
 current indices of s1 and s2 can form a substring of s3 up to the current index.
-The DP array is updated by checking if the previous state (either from s1 or s2) was true and if the current 
 character matches the corresponding character in s3.
-The final answer, dp[len(s2)], indicates whether s3 can be formed by interleaving s1 and s2.

'''
