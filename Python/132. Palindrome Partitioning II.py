# 132. Palindrome Partitioning II.

# Topic: String, Dynamic Programming.

'''
# Task:
--------
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1

Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters only.


# Testcase:
---------------
"aab"
"a"
"ab"


# Code:
-----------------
class Solution:
    def minCut(self, s: str) -> int:

'''
# Solution:
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # Create a 2D list to check if a substring is a palindrome
        # is_palindrome[i][j] will be True if the substring s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                # A substring s[j:i+1] is a palindrome if:
                # 1. The characters at the ends are equal
                # 2. The substring between the ends is a palindrome or the length of substring is less than 2
                if s[i] == s[j] and (i - j < 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True

        # Initialize a list to store the minimum cuts needed for each prefix of the string
        min_cuts = [0] * n
        for i in range(1, n):
            # If the whole substring from the start to the current position is a palindrome,
            # no cuts are needed.
            if is_palindrome[0][i]:
                min_cuts[i] = 0
            else:
                # Initialize min_cuts[i] to the maximum possible cuts (i.e., i cuts)
                min_cuts[i] = min_cuts[i - 1] + 1
                # Check for possible palindrome partitions and update min_cuts[i] accordingly
                for j in range(1, i):
                    if is_palindrome[j][i]:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j - 1] + 1)

        # Return the minimum cuts needed for the entire string
        return min_cuts[-1]

# Test cases
solution = Solution()
print(solution.minCut("aab"))  # Example 1
print(solution.minCut("a"))    # Example 2
print(solution.minCut("ab"))   # Example 3


# Description:
'''
To solve the problem of finding the minimum number of cuts needed for a palindrome partitioning 
of a string, we will use dynamic programming. The key idea is to first use dynamic programming 
to determine whether each substring is a palindrome, and then find the minimum cuts needed for 
each prefix of the string.

In this implementation:

1. We first create a 2D list is_palindrome to store whether each substring is a palindrome. This is done iteratively.
2. We then create a list min_cuts where min_cuts[i] represents the minimum number of cuts needed for the substring s[0:i+1].
3. We iterate through each character of the string. If the whole substring up to that character is a palindrome, 
   then no cuts are needed. Otherwise, we find the minimum cuts needed by checking each possible partition point.
4. Finally, we return min_cuts[-1], which represents the minimum cuts needed for the entire string.

This method efficiently computes the minimum number of cuts needed for a palindrome partitioning of the given string.

'''