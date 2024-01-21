# 139. Word Break.

# Topic: Array, Hash Table, String, Dynamic Programming, Trie, Memoization.

'''
# Task:
-------
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into 
a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.



# Testcase:
-----------
"leetcode"
["leet","code"]
"applepenapple"
["apple","pen"]
"catsandog"
["cats","dog","sand","and","cat"]



# Code:
-------
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
'''
# Solution:
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the list of words into a set for faster lookup
        wordSet = set(wordDict)  

        # Initialize a dynamic programming (DP) array with False values
        # dp[i] represents whether the substring s[:i] can be segmented
        # into words from the dictionary
        dp = [False] * (len(s) + 1)

        # Base case: empty string can always be segmented
        dp[0] = True  

        # Iterate over the length of the string
        for i in range(1, len(s) + 1):
            # Check each substring s[:j] where j is from 0 to i
            for j in range(i):
                # If s[:j] can be segmented (dp[j] is True) and
                # the remaining substring s[j:i] is a word in the dictionary,
                # then s[:i] can also be segmented
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # Once a valid segmentation is found, break the inner loop

        # Return whether the entire string can be segmented
        return dp[len(s)]

# Test cases
solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"]))  # Expected output: True
print(solution.wordBreak("applepenapple", ["apple", "pen"]))  # Expected output: True
print(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Expected output: False


'''
Description:
To solve the Word Break problem, we can use dynamic programming. The idea is to maintain a boolean 
array dp where dp[i] represents whether the substring s[:i] (the substring of s from the beginning 
up to but not including index i) can be segmented into one or more dictionary words.

The algorithm works as follows: For each position i in the string s, we check every substring s[:j] where
j is from 0 to i. If s[:j] is a valid segment (i.e., dp[j] is True) and the remaining substring s[j:i] is 
in the dictionary, then s[:i] is a valid segment.

'''


