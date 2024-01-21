# 131. Palindrome Partitioning.

# Topic: String, Dynamic Programming, Backtracking.


'''
Task:
-----
Given a string s, partition s such that every substring  of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.

# Testcase:
------------
"aab"
"a"

# Code:
-------------
class Solution:
    def partition(self, s: str) -> List[List[str]]:

'''
# Solution:
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # Precompute all palindrome substrings in the string iteratively.
        # is_palindrome[i][j] will be True if the substring s[i:j+1] is a palindrome.
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True  # A single character is always a palindrome.
            for j in range(i):
                # A substring s[j:i+1] is a palindrome if the characters at the ends are equal,
                # and if the substring s[j+1:i] is a palindrome.
                if s[j] == s[i] and (i - j == 1 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True

        # Backtracking function to build all palindrome partitions.
        def backtrack(start, path):
            # If the start index reaches the end of the string, add the current path to results.
            if start == n:
                result.append(path[:])
                return

            # Explore all possible partitions by expanding the end index.
            for end in range(start, n):
                # If the substring s[start:end+1] is a palindrome, continue backtracking.
                if is_palindrome[start][end]:
                    backtrack(end + 1, path + [s[start:end + 1]])

        result = []
        backtrack(0, [])
        return result

# Test cases
solution = Solution()
print(solution.partition("aab"))  # Example 1
print(solution.partition("a"))    # Example 2



# Description:
'''
To solve the problem of splitting a string into palindromes,we can optimize the algorithm 
by minimizing the number of recursive calls and palindrome checks. One way to achieve this
is to use an iterative approach to pre-generate all palindromic substrings, and then apply 
the backtracking method to compile partitions based on this data.

An iterative search approach for all palindromes will reduce the total number of checks performed 
during the backtracking process.

In this code:

- We first create a 2D list is_palindrome to store whether each substring is a palindrome. This is done iteratively.
- In the backtrack function, we explore all possible partitions of the string. If a substring is a palindrome 
  (as checked using is_palindrome), we continue exploring further partitions from the end of this substring.
- The function backtrack is initially called with the start index 0 and an empty path. It recursively builds up paths
  of palindromes and adds them to the result list when a complete partition of the string is found.
- The function returns all the possible palindrome partitioning of the input string s.

'''