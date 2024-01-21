"""
# 131. Palindrome Partitioning.

# Topic: String, Dynamic Programming, Backtracking.


# Task:
-----------
Given a string s, partition s such that every substring of the partition is a palindrome. 
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
-----------
"aab"
"a"


# Code:
-----------
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
"""
# Solution:
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Precompute whether each substring is a palindrome
        n = len(s)
        # Initialize a 2D array to keep track of palindrome substrings
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Fill the is_palindrome table
        for end in range(n):
            for start in range(end + 1):
                # A substring is a palindrome if:
                # 1. The end characters are the same, and
                # 2. The substring between the end characters is a palindrome (or it's a 1 or 2 character string)
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

        # Backtracking function to find palindrome partitions
        def backtrack(start, path):
            # If we reach the end of the string, add the current partition to the result
            if start == n:
                result.append(path[:])
                return
            
            # Explore all possible partitions
            for end in range(start, n):
                # If the current substring is a palindrome, continue the search with the rest of the string
                if is_palindrome[start][end]:
                    backtrack(end + 1, path + [s[start:end + 1]])

        result = []
        backtrack(0, [])
        return result

# Description:
'''
Comments Explained:

* Precomputing Palindromes: The first part of the code precomputes whether each substring of s is a palindrome. This is done using dynamic programming. A 2D array is_palindrome is initialized with False values.

* Dynamic Programming Table: The is_palindrome table is filled out such that is_palindrome[start][end] is 
  True if the substring s[start:end+1] is a palindrome. This check relies on the fact that a substring is 
  a palindrome if its first and last characters are the same and the substring between them is also a 
  palindrome.

* Backtracking Function: The backtrack function is a recursive function that builds palindrome partitions. 
  It takes the current position in the string (start) and the current list of palindromes (path) found so far.

* Recursive Partitioning: For each position start in the string, the function iterates through all possible 
  end positions. If the substring s[start:end+1] is a palindrome (checked using the is_palindrome table), 
  the function recursively calls itself with the end of the current palindrome as the new start.

* Base Case: When start reaches the end of the string (n), it means that the current path is a complete 
  partition of the string into palindromes, and it is added to the result list.

* Initialization and Execution: The list result is initialized to store the palindrome partitions. The 
  backtracking process is initiated by calling backtrack(0, []).

This solution is efficient as it minimizes redundant palindrome checks, a key factor in reducing the 
runtime for larger strings.

'''
